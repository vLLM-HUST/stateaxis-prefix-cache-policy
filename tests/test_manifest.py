import json
from pathlib import Path

from vllm_hust_ext.manifest import activation_blocker, load_manifest

import stateaxis_prefix_cache_policy


def test_manifest_is_active_but_default_off() -> None:
    root = Path(stateaxis_prefix_cache_policy.__file__).parent
    manifest = load_manifest(root / "vllm-hust-extension-v0.3.json")
    assert manifest.bundle_id == stateaxis_prefix_cache_policy.MOD_ID
    assert manifest.bundle_version == stateaxis_prefix_cache_policy.VERSION
    assert manifest.host.provider == "vllm"
    assert activation_blocker(manifest) is None
    assert manifest.activation.environment == ()
    assert manifest.activation.additional_config == ()


def test_metadata_separates_native_engine_apc() -> None:
    root = Path(stateaxis_prefix_cache_policy.__file__).parents[2]
    metadata = json.loads((root / "MOD_METADATA.json").read_text())
    assert metadata["lifecycle"]["default_enabled"] is False
    assert "the Native Engine lease-safe bounded-LRU APC implementation" in (
        metadata["scope"]["out_of_scope"]
    )


def test_qwen35_boundary_rejects_zero_hit_speedup() -> None:
    root = Path(stateaxis_prefix_cache_policy.__file__).parents[2]
    result = json.loads(
        (
            root
            / "evidence"
            / "mmlu-pro-qwen3.5-35b-boundary-20261016"
            / "RESULT.json"
        ).read_text()
    )
    assert result["eligibility_audit"]["optimistic_sequential_cache_simulation"]["hit_tokens"] == 0
    on_arm = result["successful_bracket"][1]
    assert on_arm["local_cache_query_tokens"] > 0
    assert on_arm["local_cache_hit_tokens"] == 0
    assert result["interpretation"]["causal_result"].startswith("no effect")
