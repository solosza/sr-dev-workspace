# Task 003: Shared strip_markup_then_grep Helper
**Type:** BUILD | **Gates:** GI-03
## Action
Add a shared lib helper that strips <style>/<script> blocks before grepping, and reports match context — then retrofit the portfolio absolute-claims gate to use it.
## Spec
Implement strip_markup_then_grep(html_or_source, pattern): remove <style>...</style> and <script>...</script> blocks (and inline style="..." attributes) FIRST, then apply the pattern, then return matches WITH surrounding context for adjudication. This eliminates the CSS `max-width:100%` false-positive that matched the absolute-claims grep (255/256/258). Put it in lib/ so all HTML/source semantics gates call it. Retrofit the portfolio absolute-claims gate (or its gate-contract reference) to use this helper instead of a raw grep.
## Acceptance
Helper strips <style>/<script> then greps with context; the portfolio absolute-claims gate uses it; CSS max-width:100% no longer false-positives.
