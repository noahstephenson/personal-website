Title: Research
Slug: research

<div class="case-study">

<div class="case-study-header">
<span class="case-number">01</span>
<div>
<h2>Tiered Multi-Factor Authentication System</h2>
<p class="case-meta">2026 &middot; SysML &middot; MagicDraw/Cameo &middot; Raspberry Pi &middot; Node-RED &middot; Django &middot; With Matthew Wolfe &middot; <a href="https://github.com/noahstephenson/MFA-System" target="_blank" rel="noopener">GitHub &rarr;</a></p>
</div>
</div>

<p class="case-section-label">Problem</p>

<p>Most authentication systems are built on the assumption that the network will be there when you need it. Some environments don&rsquo;t allow that. They have to work fully connected, partially degraded, or completely offline. The question was whether those conditions call for different architectures, and whether all three can still meet the same Zero Trust requirements.</p>

<p class="case-section-label">Approach</p>

<ul>
<li>Defined requirements for each connectivity tier, since latency, availability, and threat exposure change across all three</li>
<li>Built a separate SysML architecture in MagicDraw/Cameo for each tier, including components, interfaces, and behavioral constraints</li>
<li>Ran a trade study comparing all three against the same Zero Trust requirements</li>
<li>Built a Raspberry Pi prototype to test the Tier 1 assumption, with Node-RED handling sensor flow and authentication sequencing</li>
<li>Ran the prototype under simulated isolation; two interface assumptions in the model didn&rsquo;t hold up and had to be revised</li>
</ul>

<p class="case-section-label">Findings</p>

<ul>
<li>Three SysML architecture models, each with documented design rationale</li>
<li>A trade study showing that the same Zero Trust requirements can be satisfied in different ways across connectivity tiers</li>
<li>A prototype that confirmed the architecture was buildable; changes flowed both ways, with the model shaping implementation decisions and prototype failures driving two revisions to the model&rsquo;s interface specifications</li>
</ul>

</div>

<div class="case-study">

<div class="case-study-header">
<span class="case-number">02</span>
<div>
<h2>MagicGrid vs. Generic SysML</h2>
<p class="case-meta">MBSE &middot; SysML &middot; Ongoing</p>
</div>
</div>

<p>An ongoing comparison of the MagicGrid framework against a generic SysML approach, using a smart magazine as the case study. The working question: MagicGrid enforces the conceptual checkpoints defense practice expects, but does that structure earn its overhead in exploratory design?</p>

</div>

<h2>Publications</h2>

<div class="case-study">

<div class="case-study-header">
<span class="case-number">01</span>
<div>
<h2>MBSE-Guided Tiered Multi-Factor Authentication</h2>
<p class="case-meta">With Matthew Wolfe &middot; MIT IEEE URTC 2026 &middot; In preparation</p>
</div>
</div>

</div>

<div class="case-study">

<div class="case-study-header">
<span class="case-number">02</span>
<div>
<h2>MFA Beyond the Login Screen</h2>
<p class="case-meta">IEEE Potentials &middot; Under review</p>
</div>
</div>

</div>
