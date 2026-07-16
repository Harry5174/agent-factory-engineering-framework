# AFDF Extraction Provenance

This record documents how the historical Agent Factory Development Framework (AFDF) material became the provenance base for the local Agent Factory Engineering Framework (AFEF) candidate.

## Source and Method

```yaml
source_url: https://github.com/Harry5174/learn-agentic-ai
source_pin: 7990c16bc377fee8c2dc67d85a0cae2ab56b977b
historical_source_path: 03-agent-factory/development-framework/
sprint_a_archive_sha256: 91def02283f97597525df9209ea2846091503eb3e0476bea9d35adcd6de6cc85
method: seven-path selective git-filter-repo extraction with root-prefix rewrite
```

The extraction selected exactly seven paths:

1. `03-agent-factory/development-framework/README.md`
2. `03-agent-factory/development-framework/session-bootstrap.md`
3. `03-agent-factory/development-framework/docs/README.md`
4. `03-agent-factory/development-framework/docs/specs/`
5. `03-agent-factory/development-framework/docs/protocols/`
6. `03-agent-factory/development-framework/docs/templates/`
7. `03-agent-factory/development-framework/docs/memory/`

The source prefix was rewritten to the repository root. Excluded categories were project-specific memory and bootstrap packages, historical examples, historical framework evidence, stale status material, unrelated repository content, unrelated refs, and tags.

## Retained Commit Mapping

| Historical source commit | Extracted commit |
|---|---|
| `b9305a51ed84c5814fc180512aa8f985c36b8267` | `b03a6cadeb13f1b7960c76d1825a8187caf35a17` |
| `e8f75e29aa2a6ba3eb15c1dbecd31818fa274c8d` | `a8188c210558e868ac37aefc91167324806cbcf2` |
| `c84cd555222aa308a0305afc6ff08114b8fe57cd` | `0ec4bb139a3135253c8dcc78115f1367189f49f7` |
| `621a43c77bba1de414689e0e1059ae0f6f07ccc2` | `9dbd39a827b0b0ef16101732a220bf9b3db1728e` |
| `64f457c4099ac63b1a1e727fafc71ba0726cdccc` | `2ac161abe139afd74d51be3470b98f996b93a593` |

Historical commit `9383ad08867e35dc83f6d535303cf527737bd068` became empty and was removed because it changed only excluded project memory.

## Preservation and Limitations

For retained commits, the extraction preserved authorship, committer identity, author and committer timestamps, subjects, selected paths after the declared prefix rewrite, file modes, and selected blobs. The first retained commit became the extracted root because unrelated ancestry was removed.

Filtering necessarily rewrote commit hashes. Rewritten history is not byte-identical to the source history, and cryptographic commit signatures cannot generally remain valid when commit identities change. The five extraction commits remain distinguishable from subsequent AFEF canonical commits.

GitHub issues, pull requests, review comments, discussions, stars, watchers, forks, settings, branch protections, Actions run history, secrets, environments, GitHub Releases, and release discussions were not migrated because they are not part of Git history.

## Licensing Authority

The Product Owner confirmed ownership and relicensing authority for the selected scope and approved the MIT License with copyright holder `M Harry`. This statement applies only to the extracted scope and later canonical AFEF changes; it makes no claim about excluded source content.
