# StateAxis Prefix Cache Policy

Extension ID: `org.vllm-hust.stateaxis-prefix-cache-policy`

This default-off MOD lets Extension Manager own the deliberate activation of
vLLM's built-in automatic prefix cache for workloads with long repeated token
prefixes. It adds no cache algorithm and makes no novelty claim. In particular,
it is distinct from `stateaxis-automatic-prefix-cache`, the Native Engine's
lease-safe bounded-LRU research mechanism.

Status: **unmeasured experimental candidate**.

The OFF contract requires `--no-enable-prefix-caching`. When this MOD is enabled
and configured with `launch_options.enable_prefix_caching=true`, Extension
Manager removes that negative flag and appends `--enable-prefix-caching`. This
makes ON/OFF attribution explicit and keeps discovery alone inert.

Every result must record the workload hash, model, host commits, cache query/hit
counters, correctness, lifecycle, and resource release. A single screening run
cannot qualify the MOD.

Maintainer: Shuhao Zhang (Tony), directly responsible; no advisor is declared.
