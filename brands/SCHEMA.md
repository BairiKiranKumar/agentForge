# Brand profile schema

Social and design agents load one brand profile per task. Profiles live in `brands/<id>/brand.yaml`. A task names the id in the brief. Agents do not borrow voice, proof, colors, or offers from another profile.

Required keys:

| Key | Meaning |
|---|---|
| `id` | Folder name. Lowercase, no spaces. |
| `handle` | Public handle, including `@` when the platform uses one. |
| `display_name` | Name safe to print on a slide or post. |
| `owner` | Human who approves publishing. |
| `market` | Default market. |
| `locale` | Language tag, such as `en` or `en-GB`. |
| `timezone` | IANA timezone. |
| `do_not_mix_with` | Other brand ids or names that must not appear in this brand's drafts. |
| `focus` | Topics this brand is willing to be known for. |
| `voice` | Tone rules. |
| `cta` | Allowed calls to action. `publishing` stays `none` until a human approves a send. |
| `visual` | Colors and type. Agents use these values in HTML and SVG. |
| `platforms` | Sizes and limits the brand accepts. |

Rules:

1. Copy `brands/_template/brand.yaml` for a new client. Do not edit `example-brand` to serve a client. Keep real profiles in the private workspace.
2. If the brief has no brand id, ask. Do not assume `@example_brand` for client work.
3. Proof, prices, and client names come from the brief or the profile's `proof` list. Do not invent them.
4. Publishing stays unauthorized until the brief sets `authorization` per `AGENTS.md`.

Platform character limits inside a profile are working assumptions and must be re-checked in the product UI before a claim is published.
