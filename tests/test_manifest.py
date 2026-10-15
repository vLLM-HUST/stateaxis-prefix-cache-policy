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
