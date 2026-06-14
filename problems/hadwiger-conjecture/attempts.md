# Attempts — Hadwiger's Conjecture (Graph Coloring)

_Notable attempts, near-misses, retracted proofs._

## Verified cases as definitive partial results

The settled small cases are the most important "near-complete" results, because each pushes the boundary by one value of $t$ and each is, individually, a hard theorem.

- **$t=4$ (Hadwiger 1943; Dirac 1952).** A 4-chromatic graph contains a $K_4$ minor. Elementary by modern standards but the original substantive case.
- **$t=5$ (via Appel–Haken 1976).** Equivalent to the Four Color Theorem through Wagner's 1937 decomposition. It is genuinely *equivalent*, so the $t=5$ case can be regarded as proved exactly to the extent that one accepts the (computer-assisted, later Coq-formalized by Gonthier 2005) Four Color Theorem.
- **$t=6$ (Robertson–Seymour–Thomas 1993).** A minimal counterexample is apex and hence 5-colorable; this reduces $K_6$ Hadwiger to the Four Color Theorem. A landmark structural argument widely regarded as one of the deepest in the area.

## The open frontier at $t=7$

The case $t=7$ is the first genuinely open value and the natural target of focused attempts. **Kawarabayashi and Toft (2005)** proved that graphs with no $K_7$ *and* no $K_{4,4}$ minor are 6-colorable, and related partial results constrain potential counterexamples; **Jakobsen** earlier handled graphs with no $K_7^=$ (a $K_7$ with edges deleted). No full proof of $t=7$ exists, and there is no known reduction to a finite computation, which is the structural reason the case has resisted the Appel–Haken/Robertson–Seymour template.

## Asymptotic near-misses

For the quantitative version, the long-standing $\chi(G) = O(h(G)\sqrt{\log h(G)})$ (Kostochka 1980; Thomason 1984) stood as the best general bound for almost four decades — a celebrated "near-miss" that everyone believed could be improved but no one could. Its eventual improvement by **Norin–Postle–Song (2019)** and the march to $O(h(G)\log\log h(G))$ by **Delcourt–Postle (2021)** are the modern near-misses: they come within a $\log\log$ factor of the *linear* Hadwiger Conjecture but not the exact statement.

## Disputed and retracted claims

Hadwiger's Conjecture has attracted purported elementary proofs over the decades, essentially none of which has survived scrutiny; the general consensus among specialists is that no correct proof of any case $t \ge 7$ has been produced. Because the conjecture is famous and easy to state, claimed solutions circulate periodically on preprint servers and in informal venues. As a rule these are not published in refereed venues and are not accepted by the community; the standard caution applies that any claimed full proof should be treated as unverified until it appears in a peer-reviewed journal and is independently checked. This dossier does not endorse any specific claimed proof. The *neutral, citable* state of the art is: $t \le 6$ proved (with $t=5,6$ resting on the Four Color Theorem), $t \ge 7$ open, and the best general bound $O(h(G)\log\log h(G))$.

## A cautionary structural lesson

An instructive "warning" near-miss is the relationship to **Hajós' Conjecture** ($\chi(G) \ge t \Rightarrow G$ contains a *topological* $K_t$, i.e. a subdivision). Hadwiger's is the minor version; Hajós' is the stronger subdivision version. **Catlin (1979)** disproved Hajós' Conjecture for $t \ge 7$, and **Erdős–Fajtlowicz (1981)** showed it fails for almost all graphs. This does not refute Hadwiger's Conjecture — minors are weaker than subdivisions, so Hadwiger can hold where Hajós fails — but it is a standing reminder that the analogous, slightly stronger statement is *false*, and that intuitive arguments must respect the minor/subdivision distinction. It tempers optimism that a simple counting or extremal argument will close Hadwiger's gap.
