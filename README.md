# StateAxis Prefix Cache Policy

Extension ID: `org.vllm-hust.stateaxis-prefix-cache-policy`

This default-off MOD lets Extension Manager own the deliberate activation of
vLLM's built-in automatic prefix cache for workloads with long repeated token
prefixes. It adds no cache algorithm and makes no novelty claim. In particular,
it is distinct from `stateaxis-automatic-prefix-cache`, the Native Engine's
lease-safe bounded-LRU research mechanism.

Status: **workload-scoped experimental positive; not performance-qualified**.

The OFF contract requires `--no-enable-prefix-caching`. When this MOD is enabled
and configured with `launch_options.enable_prefix_caching=true`, Extension
Manager removes that negative flag and appends `--enable-prefix-caching`. This
makes ON/OFF attribution explicit and keeps discovery alone inert.

On the materialized MMLU-Pro performance workload, three fresh-service,
alternating-order Qwen3-8B ON/OFF pairs showed a median output-throughput delta
of **+11.00%**, median mean-TTFT delta of **-15.39%**, and median mean-TPOT
delta of **-5.68%**. All arms completed 40/40 requests, and every ON arm
recorded 40,960 token hits from 55,102 queries (74.34%). This is a repeated,
real-online, workload-scoped experimental result—not a Qwen3.5-35B result,
accuracy score, general performance claim, or official qualification. See
[`evidence/mmlu-pro-qwen3-8b-repeated-20261015/RESULT.json`](evidence/mmlu-pro-qwen3-8b-repeated-20261015/RESULT.json).

Every result must record the workload hash, model, host commits, cache query/hit
counters, correctness, lifecycle, and resource release. Official
Qwen3.5-35B-A3B TP2 confirmation and output exactness remain qualification
gates.

Maintainer: Shuhao Zhang (Tony), directly responsible; no advisor is declared.
