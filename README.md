# StateAxis Prefix Cache Policy

Extension ID: `org.vllm-hust.stateaxis-prefix-cache-policy`

This default-off MOD lets Extension Manager own the deliberate activation of
vLLM's built-in automatic prefix cache for workloads whose repeated token
prefix reaches at least one effective host cache page. It adds no cache
algorithm and makes no novelty claim. In particular,
it is distinct from `stateaxis-automatic-prefix-cache`, the Native Engine's
lease-safe bounded-LRU research mechanism.

Status: **workload-scoped experimental positive; not performance-qualified**.

The OFF contract requires `--no-enable-prefix-caching`. When this MOD is enabled
and configured with `launch_options.enable_prefix_caching=true`, Extension
Manager removes that negative flag and appends `--enable-prefix-caching`. This
makes ON/OFF attribution explicit and keeps discovery alone inert.

Original measured figures, raw records, failed attempts and limitations are now
maintained in [benchmark's frozen report](https://github.com/vLLM-HUST/vllm-hust-benchmark/blob/ddc4f6a3290e447260fc8f6c03ea36d3ca514e23/archive/mod-git-20261021/stateaxis-prefix-cache-policy/snapshot/README.md) and
[original evidence index](https://github.com/vLLM-HUST/vllm-hust-benchmark/blob/ddc4f6a3290e447260fc8f6c03ea36d3ca514e23/archive/mod-git-20261021/stateaxis-prefix-cache-policy/snapshot/evidence/mmlu-pro-qwen3.5-35b-boundary-20261016/README.md). See [EVIDENCE.md](EVIDENCE.md)
for immutable source links and verified external-cache retrieval.

The repeated-prefix workload result and the official hybrid-cache negative
boundary are separate experiments. The latter did not exercise cache reuse;
the apparent cold-first gain is rejected by the warmed trailing OFF control.
Its [original boundary result](https://github.com/vLLM-HUST/vllm-hust-benchmark/blob/ddc4f6a3290e447260fc8f6c03ea36d3ca514e23/archive/mod-git-20261021/stateaxis-prefix-cache-policy/snapshot/evidence/mmlu-pro-qwen3.5-35b-boundary-20261016/RESULT.json)
remains an input to the regression test, downloaded and verified before reading.

Every result must record the workload hash, model, host commits, cache query/hit
counters, correctness, lifecycle, and resource release.
Before enabling this MOD, tokenize the exact workload and compare shared-prefix
lengths with the model/runtime's effective cache page. Output exactness and a
representative long-prefix Qwen3.5-35B-A3B TP2 run remain qualification gates.

Maintainer: Shuhao Zhang (Tony), directly responsible; no advisor is declared.
