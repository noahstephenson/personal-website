Title: Research
Slug: research

<div class="case-study">

<div class="case-study-header">
<span class="case-number">01</span>
<div>
<h2>Tiered Multi-Factor Authentication System</h2>
<p class="case-meta">Systems Engineering &middot; 2026 &middot; SysML &middot; MagicDraw/Cameo &middot; Raspberry Pi &middot; Node-RED &middot; Django &middot; <a href="https://github.com/noahstephenson/MFA-System" target="_blank" rel="noopener">GitHub &rarr;</a></p>
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
<li>A prototype that confirmed the architecture was buildable and exposed issues the model alone did not catch</li>
</ul>

</div>

<div class="case-study">

<div class="case-study-header">
<span class="case-number">02</span>
<div>
<h2>Paper Trading Web Application</h2>
<p class="case-meta">Full-Stack Engineering &middot; 2023 &middot; Django &middot; Python</p>
</div>
</div>

<p class="case-section-label">Problem</p>

<p>The interesting part of a trading simulator isn&rsquo;t the interface. It&rsquo;s getting the underlying system right: auth flows, transaction integrity, consistent portfolio state.</p>

<p class="case-section-label">Approach</p>

<ul>
<li>Designed the data model: users, positions, transaction history, market data</li>
<li>Built authentication and session management with Django</li>
<li>Implemented trade execution logic using live market data to enforce real transaction constraints</li>
</ul>

<p class="case-section-label">Outcome</p>

<ul>
<li>Full application handling auth, trade execution, and persistent portfolio state</li>
<li>Built end-to-end &mdash; data model to deployed interface</li>
</ul>

</div>
