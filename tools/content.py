# Page content for standardspaceworx.space. Proprietary to Standard Data Company.
# Style: no em dashes anywhere. Brand is always "Standard SpaceWorX".

SITE = "https://standardspaceworx.space"
LASTMOD = "2026-10-22"

# Analytics IDs. Leave empty to omit the tags entirely.
GTM_ID = ""
GA4_ID = ""

ORG = {
    "name": "Standard SpaceWorX",
    "parent": "Standard Data Company",
    "parentUrl": "https://standarddatacompany.net",
    "email": "contact@standardspaceworx.space",
    "founder": "Doug Mangeris",
    "foundingDate": "2026",
    "description": "Standard SpaceWorX builds Terrier reusable satellites that capture orbital debris and return to a parked orbit for the next job. A Standard Data Company venture in Loveland, Colorado.",
    # Add live public profile URLs here as they are confirmed.
    "sameAs": [],
}

CTA_BAND = """
<section class="back">
  <div class="wrap">
    <div>
      <div class="eyebrow">Work with us</div>
      <h2>Clearing orbit is a fleet job</h2>
      <p>Investors, satellite operators, government and defense buyers, and aerospace partners can reach the founder directly. We respond to every serious inquiry.</p>
    </div>
    <div class="side">
      <a class="btn solid" href="/contact/">Contact Standard SpaceWorX</a>
      <p>Investor inquiries: <a href="mailto:contact@standardspaceworx.space">contact@standardspaceworx.space</a></p>
    </div>
  </div>
</section>
"""


def related(items):
    lis = "".join('<li><a href="%s">%s</a></li>' % (h, t) for h, t in items)
    return '<aside class="related"><h2>Continue reading</h2><ul>' + lis + "</ul></aside>"


# ---------------------------------------------------------------- HOME
HOME_BODY = """
<section class="hero">
  <div class="wrap">
    <div>
      <div class="eyebrow">A Standard Data Company venture</div>
      <p class="wordmark" aria-hidden="true">Standard<br>SpaceWor<span class="x">X</span></p>
      <h1>Reusable satellites for space debris removal</h1>
      <p class="sub">Every debris removal vehicle flown so far dies with its first target. Standard SpaceWorX builds Terriers: reusable servicer satellites that maneuver to a piece of orbital debris, capture it, dispose of it, and return to a parked orbit for the next job.</p>
      <p class="tag">Clear the plane. Keep the plane. Lease the plane.</p>
      <div class="cta-row">
        <a class="btn solid" href="/investors/">For Investors</a>
        <a class="btn ghost" href="/technology/terrier/">Meet the Terrier</a>
      </div>
      <div class="plate"><span class="rvt"></span>
        <p class="plate-title">Terrier mission spec plate</p>
        <div class="specgrid">
          <div class="spec"><div class="k">Home plane</div><div class="v">98.8<em> deg</em></div></div>
          <div class="spec"><div class="k">Altitude</div><div class="v">865<em> km</em></div></div>
          <div class="spec"><div class="k">Thruster Isp</div><div class="v">2000<em> s</em></div></div>
          <div class="spec"><div class="k">Missions per tank</div><div class="v"><em>45</em></div></div>
        </div>
      </div>
    </div>
    <div class="orbit-stage" aria-hidden="true">
      <div class="planet"></div>
      <div class="ring"></div>
      <div class="ring r2"></div>
    </div>
  </div>
</section>

<section class="score" id="problem" aria-labelledby="problem-h">
  <div class="wrap">
    <h2 id="problem-h" class="eyebrow" style="grid-column:1/-1;margin:0;font-size:14px">The problem in three numbers</h2>
    <div>
      <div class="big">$1B+</div>
      <div class="cap">committed to space debris removal programs over the last decade</div>
    </div>
    <div>
      <div class="big o">0</div>
      <div class="cap">pieces of uncooperative legacy debris removed from orbit so far</div>
    </div>
    <div>
      <div class="big">5-10</div>
      <div class="cap">large objects removed per year is the published threshold for stabilizing low Earth orbit</div>
    </div>
  </div>
</section>

<section id="work">
  <div class="wrap">
    <div class="eyebrow">The work</div>
    <h2>One vehicle. Three revenue streams.</h2>
    <p class="lede">A Terrier lives in orbit, works a route, and earns in three ways while it does. Reuse is what turns active debris removal from a grant-funded demonstration into a business.</p>
    <div class="streams">
      <article class="stream">
        <div class="n">REVENUE 01</div>
        <h3>Active debris removal</h3>
        <p>Each Terrier is assigned to one orbital plane, the way a crew is assigned to one job site. It parks dormant, wakes on tasking, phases to the target, captures it, disposes of it, and returns.</p>
        <p>Reusing one vehicle across dozens of targets moves the cost per object from the industry's 90 million dollar class toward the 3 to 8 million dollar class.</p>
      </article>
      <article class="stream">
        <div class="n">REVENUE 02</div>
        <h3>Earth observation data</h3>
        <p>The home plane is sun synchronous orbit, the most valuable imaging orbit in space. Between jobs the Terrier's camera points down and collects imagery for sale.</p>
        <p>The camera is ours alone. We do not sell imaging or recording space on the vehicle; the data business stays in house.</p>
      </article>
      <article class="stream">
        <div class="n">REVENUE 03</div>
        <h3>Hosted communications payloads</h3>
        <p>Spare mass, power, and pointing on each Terrier is leased to communications tenants, the way carriers lease space on a cell tower.</p>
        <p>Transmit and receive hardware only. No cameras, no recorders, no exceptions.</p>
      </article>
    </div>
    <h3 style="margin-top:44px">The Terrier mission cycle</h3>
    <div class="cycle">
      <div class="step"><div class="num">01</div><h4>Park</h4><p>Dormant, low power, camera earning</p></div>
      <div class="step"><div class="num">02</div><h4>Wake</h4><p>Tasking received from the ground</p></div>
      <div class="step"><div class="num">03</div><h4>Phase</h4><p>Drop 25 km, lap forward to target</p></div>
      <div class="step hot"><div class="num">04</div><h4>Capture</h4><p>Grapple the tumbling target</p></div>
      <div class="step"><div class="num">05</div><h4>Dispose</h4><p>Deorbit assist, boost, or handoff</p></div>
      <div class="step"><div class="num">06</div><h4>Return</h4><p>Back to park. Repeat up to 45 times per tank</p></div>
    </div>
    <p style="margin-top:22px"><a href="/technology/terrier/">Read the full Terrier program overview</a></p>
  </div>
</section>

<section class="sheet" id="planes">
  <div class="wrap">
    <div class="eyebrow">Job sites</div>
    <h2>Three planes hold the priority mass</h2>
    <p class="lede">Debris is not spread evenly across the sky. It is clustered in a handful of orbital planes, and three of them hold an estimated 80 percent of the mass that matters.</p>
    <div class="titleblock">
      <div class="tb-head"><span>Standard SpaceWorX</span><span>DWG: Priority Plane Schedule</span><span>Rev B</span></div>
      <div class="tb-row">
        <div>98&deg;</div>
        <div class="alt">SSO / 700-1,100 km</div>
        <div class="desc">Fengyun-1C fragment cloud (thousands of tracked pieces), Envisat and H-2 class heavy derelicts. Also the plane the orbital data center industry is filing to occupy.</div>
        <div class="camp">CAMPAIGN 1</div>
      </div>
      <div class="tb-row dim">
        <div>71&deg;</div>
        <div class="alt">840 km</div>
        <div class="desc">Eighteen SL-16 rocket bodies at roughly 8,300 kg each. A collision between any two would roughly double the low Earth orbit debris catalog.</div>
        <div class="camp">CAMPAIGN 2</div>
      </div>
      <div class="tb-row dim">
        <div>74-83&deg;</div>
        <div class="alt">780-980 km</div>
        <div class="desc">SL-8 rocket body fleets. Hundreds of 1,400 kg class bodies, more than forty years on orbit, never coming down on their own.</div>
        <div class="camp">CAMPAIGN 3</div>
      </div>
    </div>
    <p style="margin-top:22px"><a href="/mission/">Why reusable removal is the only way to clear these planes</a></p>
  </div>
</section>

<section id="why">
  <div class="wrap">
    <div class="eyebrow">Why now</div>
    <h2>The 2027 to 2030 convergence</h2>
    <div class="now-grid">
      <div class="now">
        <h3>Regulation with teeth</h3>
        <p>The FCC five year disposal rule is in force and the first debris fine has been levied. ESA requires 90 percent disposal success. Insurers now ask for debris compliance before writing policies.</p>
      </div>
      <div class="now">
        <h3>Tenants are moving in</h3>
        <p>Gigawatt scale orbital data center constellations have filed for sun synchronous orbit, the same band the worst debris contaminates. Somebody has to clear the site before they move in.</p>
      </div>
      <div class="now">
        <h3>Launch costs are falling</h3>
        <p>Next generation launch pricing makes a standardized, mass produced servicer fleet affordable for the first time. Rideshare to our first plane is already routine.</p>
      </div>
    </div>
    <div class="cards">
      <div class="card">
        <h3>Investors</h3>
        <p>Stage, what has been built, the roadmap from ground prototype to first campaign, and how to reach the founder.</p>
        <a class="more" href="/investors/">Investor overview</a>
      </div>
      <div class="card">
        <h3>Latest updates</h3>
        <p>Policy, orbital debris science, and the Colorado space economy, written for operators and investors.</p>
        <a class="more" href="/news/">News and updates</a>
      </div>
    </div>
  </div>
</section>
""" + CTA_BAND

# ---------------------------------------------------------------- TERRIER
TERRIER_BODY = """
<section class="page-hero">
  <div class="wrap narrow">
    {crumbs}
    <div class="eyebrow">Technology</div>
    <h1>The Terrier: a reusable servicing satellite built for capture</h1>
    <p class="lede">The Terrier is the Standard SpaceWorX removal vehicle. It is a reusable servicing satellite that lives in one orbital plane, phases to a debris target, captures it, disposes of it, and returns to a parked orbit to wait for the next job.</p>
  </div>
</section>
<section class="article">
  <div class="wrap narrow prose">
    <h2>Why we call it a Terrier</h2>
    <p>Terriers were bred to go into the ground after something that does not want to be caught, bring it out, and go back in. That is the job. A Terrier satellite is small relative to the objects it hunts, it is persistent, and it works a defined territory rather than roaming. The name also signals something about the design philosophy: this is a working vehicle, not a one-off science demonstration.</p>

    <h2>The problem with single-use removal vehicles</h2>
    <p>Every active debris removal mission flown or contracted to date follows the same pattern. A chaser spacecraft launches, rendezvous with one target, attaches to it, and then deorbits with it. The chaser is consumed. The cost of the entire vehicle, its launch, and its operations team is charged to one object. That is how a single removal ends up in the 90 million dollar class, and it is why, after more than a billion dollars committed across the industry, no uncooperative legacy debris object has yet been removed from orbit.</p>
    <p>At that price, removal is a demonstration budget line, not a service. The published models for stabilizing low Earth orbit call for removing five to ten large objects per year, every year, for decades. Single-use vehicles cannot do that at any budget a customer will pay.</p>

    <h2>How the Terrier changes the math</h2>
    <p>The Terrier separates the expensive part of the system from the consumable part. The vehicle, its propulsion, its guidance and navigation stack, and its capture mechanism are reused across many targets. The only thing consumed per mission is propellant and a small amount of hardware life. Spread the fixed cost over dozens of jobs and the cost per object moves toward the 3 to 8 million dollar class, which is a number operators, insurers, and governments can budget against.</p>
    <table>
      <thead><tr><th>Parameter</th><th>Reference value</th><th>Why it matters</th></tr></thead>
      <tbody>
        <tr><td>Home plane</td><td>98.8 degrees inclination</td><td>Sun synchronous orbit, where the heaviest priority debris sits and where the most valuable imaging happens</td></tr>
        <tr><td>Parking altitude</td><td>865 km</td><td>Above the densest fragment bands, below the heavy derelicts, with low drag for long dormant periods</td></tr>
        <tr><td>Propulsion</td><td>Electric, 2000 s specific impulse</td><td>High efficiency phasing and return legs so one tank covers many missions</td></tr>
        <tr><td>Missions per tank</td><td>Up to 45</td><td>The reuse count that drives cost per object down by an order of magnitude</td></tr>
        <tr><td>Phasing maneuver</td><td>Drop 25 km, lap forward</td><td>Standard, repeatable approach geometry that keeps every mission on a known playbook</td></tr>
      </tbody>
    </table>
    <p>These are design reference values from the Standard SpaceWorX satellite design reference package. They are the baseline the engineering prototype is being built against and they will be updated as the program matures.</p>

    <h2>The mission cycle</h2>
    <figure>
      <img src="/assets/img/terrier-mission-cycle.svg" width="1200" height="520" alt="Diagram of the six step Terrier mission cycle around Earth: park in sun synchronous orbit, wake on tasking, phase down 25 km to the target, capture the tumbling debris object, dispose by deorbit assist or boost, and return to the parked orbit" loading="lazy">
      <figcaption>The Terrier mission cycle. Each loop consumes propellant only; the vehicle is retained.</figcaption>
    </figure>
    <ol>
      <li><strong>Park.</strong> The Terrier sits dormant at 865 km in its home plane, drawing minimal power. The downward facing camera collects Earth observation imagery while it waits.</li>
      <li><strong>Wake.</strong> Ground operations issue tasking against a specific catalog object in the same plane. The vehicle brings up its navigation sensors and propulsion.</li>
      <li><strong>Phase.</strong> The Terrier drops roughly 25 km to a faster orbit and laps forward until it closes on the target, then climbs back to match.</li>
      <li><strong>Capture.</strong> Close proximity operations, characterization of the target's tumble, and a mechanical grapple. This is the hardest step and the one the ground prototype program is focused on.</li>
      <li><strong>Dispose.</strong> Depending on the object and the customer, the Terrier provides a deorbit assist to a short-lived altitude, boosts the object to a disposal orbit, or hands it to a third party disposal vehicle.</li>
      <li><strong>Return.</strong> The Terrier releases, climbs back to the parking altitude, and goes dormant again. Then it does the whole thing again, up to 45 times per tank.</li>
    </ol>

    <h2>Satellite capture: the engineering focus</h2>
    <p>Rendezvous and proximity operations are well understood. Capture of an uncooperative, tumbling object is not routine, and it is where single-use programs have spent most of their money and schedule. The Terrier approach is to standardize the problem rather than solve each target as a bespoke mission. A finite set of target classes, a finite set of approach geometries, and a capture mechanism designed for the common features of rocket bodies and large derelicts, rather than one custom interface per object.</p>
    <p>Standard SpaceWorX has completed a patent landscape study covering more than forty capture, servicing, and removal patents to map what is already claimed, what has expired, and where the open design space is. The engineering prototype program begins with the capture mechanism on the ground, under representative lighting and motion, before anything flies.</p>

    <h2>What a Terrier does between jobs</h2>
    <p>A debris removal vehicle that only earns when it is removing debris is idle most of its life. The Terrier is designed so that idle time earns. The home plane is sun synchronous, which means the same ground lighting on every pass, the orbit commercial imaging companies pay the most for. The Terrier's own camera collects imagery during dormant periods. Spare mass, power, and pointing budget on the vehicle is leased to hosted communications payloads, transmit and receive hardware only. Those two revenue streams run whether or not a removal contract is active, which is what makes a Terrier fleet financeable before the removal market is fully priced.</p>

    <h2>The first campaign</h2>
    <p>The first Terrier campaign targets the 98 degree sun synchronous plane between 700 and 1,100 km. That plane holds the Fengyun-1C fragment cloud, Envisat, and several heavy upper stages, and it is the same band that large orbital data center constellations have filed to occupy. It is the highest value plane to clear and the most valuable plane to be parked in afterward. Subsequent campaigns move to the 71 degree SL-16 cluster at 840 km and the SL-8 fleets between 74 and 83 degrees.</p>

    <h2>Who the Terrier program serves</h2>
    <ul>
      <li><strong>Satellite operators</strong> who need a specific object moved out of their shell, or who need a disposal partner to meet regulatory requirements.</li>
      <li><strong>Government and defense buyers</strong> with catalog objects of concern and a need for a domestic, repeatable removal capability.</li>
      <li><strong>Aerospace partners</strong> in launch, propulsion, sensors, and ground operations who want to be on the vehicle.</li>
      <li><strong>Investors</strong> who want exposure to on-orbit servicing through a model with recurring revenue rather than one-off contracts. See the <a href="/investors/">investor overview</a>.</li>
    </ul>
    <div class="callout">
      <p>Program status: design reference package complete, patent landscape study complete, ground prototype of the capture system in planning. Inquiries to <a href="mailto:contact@standardspaceworx.space">contact@standardspaceworx.space</a> or through the <a href="/contact/">contact form</a>.</p>
    </div>
""" + related([
    ("/mission/", "Mission: why reusable beats single-use deorbit"),
    ("/investors/", "Investor overview"),
    ("/news/kessler-syndrome-solutions/", "Kessler syndrome solutions that actually stabilize orbit"),
    ("/about/", "About Standard SpaceWorX and Standard Data Company"),
]) + """
  </div>
</section>
""" + CTA_BAND

# ---------------------------------------------------------------- MISSION
MISSION_BODY = """
<section class="page-hero">
  <div class="wrap narrow">
    {crumbs}
    <div class="eyebrow">Mission</div>
    <h1>Active debris removal only works if the vehicle comes back</h1>
    <p class="lede">The mission of Standard SpaceWorX is to make active debris removal a repeatable, priced service rather than a series of one-off demonstrations. The way to do that is to stop throwing the vehicle away.</p>
  </div>
</section>
<section class="article">
  <div class="wrap narrow prose">
    <h2>The state of the problem</h2>
    <p>Low Earth orbit holds tens of thousands of tracked objects larger than ten centimeters and far more that are too small to track but large enough to end a mission. Most of the mass is not in small fragments. It is in a few thousand large derelicts: dead satellites and spent upper stages that have been in orbit for decades and will stay there for centuries. When two of them collide, the result is not two pieces of debris but thousands, and each of those becomes a new collision risk. That feedback loop is the Kessler syndrome, and the concentration of heavy objects in a handful of orbital planes is what makes it a near-term concern rather than a theoretical one.</p>
    <p>The research consensus on what it takes to stabilize the environment has been stable for more than a decade: remove on the order of five to ten of the largest, highest-risk objects every year, prioritized by mass and collision probability, in addition to the post-mission disposal rules that now apply to new satellites. Mitigation rules keep the problem from getting worse. Only removal makes it better.</p>

    <h2>What single-use deorbit actually costs</h2>
    <p>The debris removal missions that have been flown or contracted so far share an architecture. One chaser spacecraft, one target, one deorbit, and the chaser burns up with the target. Every dollar of vehicle development, launch, and operations is amortized over a single object. The result is programs in the 90 million dollar class per object, funded by space agencies as technology demonstrations.</p>
    <p>At that cost, a stabilization campaign of ten objects per year would run close to a billion dollars annually, forever. No customer exists for that. Satellite operators will not pay it, insurers will not underwrite against it, and governments fund it only as research. The architecture is the reason the market has not formed.</p>
    <p>There is a second cost that is easier to miss. Each single-use mission is a bespoke engineering program. The capture interface is designed for one target, the approach is planned for one tumble state, and the team disbands or moves on afterward. Nothing compounds. The second mission is nearly as expensive as the first.</p>

    <h2>Why reusable removal is different</h2>
    <p>A reusable servicer separates the expensive part of the system, the vehicle, from the consumable part, the propellant. The Standard SpaceWorX <a href="/technology/terrier/">Terrier</a> is designed to perform up to 45 removal missions on one tank of propellant. The vehicle cost, the launch cost, and the operations team are spread across all of them. Cost per object moves from the 90 million dollar class toward the 3 to 8 million dollar class, which is the range where a disposal contract looks like an insurance premium rather than a national program.</p>
    <p>Reuse also changes the engineering. When one vehicle will capture dozens of objects, it has to be designed for a class of targets rather than one target, and the capture procedure has to be a repeatable playbook rather than a custom plan. That discipline is harder up front and far cheaper over a campaign. It is the same shift that happened when launch went from expendable to reusable: the first reusable vehicle is more expensive to design, and every flight after that is cheaper than anything the old model could offer.</p>

    <h2>Plane-locked operations</h2>
    <p>Changing orbital planes is the most expensive maneuver in low Earth orbit. A vehicle that tries to serve every plane spends its propellant getting between jobs rather than doing them. The Terrier concept assigns each vehicle to one plane, the way a construction crew is assigned to one job site, and works that plane until it is clear. The three priority planes, the 98 degree sun synchronous band, the 71 degree SL-16 cluster, and the 74 to 83 degree SL-8 fleets, together hold an estimated 80 percent of the mass that matters. Three plane-locked campaigns address most of the problem.</p>
    <p>A plane-locked vehicle has another advantage. When it is not removing debris, it is still in a useful orbit. In sun synchronous orbit that means it can collect Earth observation imagery and host communications payloads between jobs. The vehicle earns while it waits, which is what makes a removal fleet financeable before the removal market is fully priced.</p>

    <h2>Removal is becoming a compliance requirement</h2>
    <p>Three things changed between 2022 and 2026 that turn debris removal from a public good into a purchasable service. First, regulators now enforce disposal. The FCC's five year post-mission disposal rule is in effect and the agency has issued its first enforcement action against an operator for a failed disposal. ESA's mitigation requirements call for a 90 percent probability of successful disposal. Second, insurers have started asking about disposal plans before writing policies. Third, new large constellations, including gigawatt-scale orbital data center proposals, have filed for the exact sun synchronous band where the heaviest legacy debris sits. Operators with billions committed to a plane have a direct interest in clearing it.</p>
    <p>None of these developments create demand for a 90 million dollar removal. All of them create demand for a 3 to 8 million dollar one.</p>

    <h2>What we are building toward</h2>
    <ol>
      <li><strong>A ground-proven capture system.</strong> The hardest step in the cycle is grappling a tumbling, uncooperative object. The Terrier program starts there, on the ground, before anything flies.</li>
      <li><strong>A first Terrier in the 98 degree plane.</strong> One vehicle, one plane, a demonstration on a cooperative target followed by the first commercial removals.</li>
      <li><strong>A standing fleet.</strong> Terriers parked in each priority plane, tasked by operators, insurers, and governments, earning imaging and hosted payload revenue between removals.</li>
    </ol>
    <p>The <a href="/investors/">investor overview</a> covers stage and roadmap. The <a href="/technology/terrier/">Terrier page</a> covers the vehicle. The <a href="/news/">news section</a> tracks policy and the orbital environment as they evolve.</p>

    <h2>Our commitments</h2>
    <ul>
      <li>We publish our design reference values and update them as the program matures, so partners can plan against real numbers.</li>
      <li>The imaging on our vehicles is ours. We do not sell camera or recorder space to tenants.</li>
      <li>Hosted payloads are transmit and receive hardware only.</li>
      <li>We operate from Loveland, Colorado, inside one of the deepest aerospace labor markets in the United States, and we build domestic capability.</li>
    </ul>
""" + related([
    ("/technology/terrier/", "The Terrier reusable capture satellite"),
    ("/news/fcc-five-year-rule-orbital-debris-mitigation/", "The FCC five year rule and orbital debris mitigation"),
    ("/news/kessler-syndrome-solutions/", "Kessler syndrome solutions that work"),
    ("/investors/", "Investor overview"),
]) + """
  </div>
</section>
""" + CTA_BAND

# ---------------------------------------------------------------- INVESTORS
INVESTORS_BODY = """
<section class="page-hero">
  <div class="wrap narrow">
    {crumbs}
    <div class="eyebrow">Investors</div>
    <h1>A Colorado space startup building the reusable debris removal fleet</h1>
    <p class="lede">Standard SpaceWorX is an early stage aerospace venture based in Loveland, Colorado. This page covers where the company stands, what has been built, the roadmap, and how to reach the founder. It is written for institutional and strategic investors who already know the on-orbit servicing market and want the specifics.</p>
  </div>
</section>
<section class="article">
  <div class="wrap narrow prose">
    <h2>The thesis in one paragraph</h2>
    <p>Active debris removal has absorbed more than a billion dollars of program funding without removing a single uncooperative legacy object, because every vehicle built so far is consumed by its first job. A reusable servicer that performs dozens of removals per tank of propellant moves the cost per object from the 90 million dollar class toward the 3 to 8 million dollar class. At that price, removal becomes a compliance and insurance line item that satellite operators, insurers, and governments will pay for repeatedly. The same vehicle earns Earth observation and hosted payload revenue between removals, so the fleet generates revenue before the removal market is fully priced. Standard SpaceWorX is building that vehicle, the <a href="/technology/terrier/">Terrier</a>, and the plane-locked fleet model around it.</p>

    <h2>Stage</h2>
    <p>Standard SpaceWorX is pre-seed. The company operates as a venture of Standard Data Company, a Loveland, Colorado S corporation that holds all Standard SpaceWorX intellectual property. We are raising to fund the ground prototype of the Terrier capture system and the engineering team to build it. There is no outside capital in the company today.</p>

    <h2>What has been built</h2>
    <ul>
      <li><strong>Mission architecture.</strong> The plane-locked, reusable servicer model, the three priority campaign planes, and the three revenue stream structure described across this site.</li>
      <li><strong>Satellite design reference package.</strong> A reference design for the Terrier vehicle covering orbit, propulsion sizing, mission cycle, and the 45 missions per tank reuse baseline.</li>
      <li><strong>Patent landscape study.</strong> A review of more than forty capture, servicing, and debris removal patents mapping what is claimed, what has expired, and where the open design space for a standardized capture mechanism sits.</li>
      <li><strong>Corporate structure and brand.</strong> The venture, its IP ownership, its public presence, and its investor and partner channels.</li>
    </ul>

    <h2>Roadmap</h2>
    <p>The roadmap is sequenced so that each phase retires the largest remaining technical risk before the next phase spends capital on flight hardware. Milestone dates are tied to funding and are shared with investors in diligence rather than published here.</p>
    <table>
      <thead><tr><th>Phase</th><th>Objective</th><th>Risk retired</th></tr></thead>
      <tbody>
        <tr><td>0. Foundation</td><td>Design reference, patent landscape, pre-seed raise</td><td>Is there a defensible, buildable architecture</td></tr>
        <tr><td>1. Ground prototype</td><td>Capture mechanism and proximity operations tested on the ground against representative tumbling targets</td><td>Can a standardized mechanism capture the common target classes</td></tr>
        <tr><td>2. First Terrier</td><td>Flight unit on rideshare to the 98 degree plane, demonstration on a cooperative target, first commercial removals</td><td>Does the full mission cycle close on orbit</td></tr>
        <tr><td>3. Campaign 1</td><td>Standing Terrier capacity in sun synchronous orbit, imaging and hosted payload revenue live</td><td>Does the three revenue model finance the fleet</td></tr>
        <tr><td>4. Campaigns 2 and 3</td><td>Additional Terriers in the 71 degree and 74 to 83 degree planes</td><td>Fleet scale economics</td></tr>
      </tbody>
    </table>

    <h2>Why the window is 2027 to 2030</h2>
    <p>Regulation now has enforcement behind it: the FCC five year disposal rule is in force and the first fine has been issued, and ESA requires a 90 percent probability of successful disposal. Insurers have started asking about disposal before writing policies. Multiple large constellations, including gigawatt-scale orbital data center filings, target the same sun synchronous band where the heaviest legacy debris sits, which gives well-capitalized operators a direct reason to pay for clearing it. And next generation launch pricing makes a standardized servicer fleet affordable to deploy for the first time. A company that has a working capture system and a vehicle in the plane when that demand arrives is positioned to take the market. One that starts then is not.</p>

    <h2>Use of proceeds</h2>
    <p>The current raise funds the Phase 1 ground prototype: the capture mechanism, the test rig for representative tumbling targets, the guidance and navigation simulation, and the core engineering hires to run the program. Investors in diligence receive the detailed budget, hiring plan, and the design reference package.</p>

    <h2>Why Colorado</h2>
    <p>Colorado has one of the largest aerospace economies in the United States, anchored by Space Force installations in Colorado Springs and Aurora, prime contractors and satellite manufacturers along the Front Range, and university programs at Boulder and Fort Collins that produce spacecraft engineers every year. Loveland sits in Northern Colorado, inside commuting range of Fort Collins and Boulder and within reach of the Denver aerospace cluster. For a company whose first hires are propulsion, GNC, and mechanisms engineers, this is the right labor market, and it is a domestic one, which matters to government and defense buyers.</p>

    <h2>Leadership</h2>
    <p>Standard SpaceWorX was founded by Doug Mangeris, who serves as Chief Executive Officer. His background is field operations and large capital projects: commercial construction superintendent on more than 230 million dollars of delivered work across healthcare, multifamily, senior living, retail, and industrial, and before that upstream oil and gas drilling. That background shapes the company's approach. Debris removal is treated as a fleet operations and logistics problem with a hard engineering core, not as a research program. The <a href="/about/">about page</a> has more on the founder and on Standard Data Company.</p>

    <h2>How to get in touch</h2>
    <p>Investor inquiries go directly to the founder. Email <a href="mailto:contact@standardspaceworx.space?subject=Investor%20Inquiry%20-%20Standard%20SpaceWorX">contact@standardspaceworx.space</a> with a short note on your fund or strategic interest, or use the <a href="/contact/">contact form</a> and select Investor as the inquiry type. We respond to every serious inquiry and we will share the design reference package, the patent study, and the Phase 1 plan under NDA.</p>
    <div class="callout">
      <p>This page is informational. It is not an offer to sell or a solicitation of an offer to buy any security. Any offering will be made only to qualified investors through definitive documents.</p>
    </div>
""" + related([
    ("/technology/terrier/", "The Terrier reusable capture satellite"),
    ("/mission/", "Mission: why reusable beats single-use deorbit"),
    ("/news/front-range-space-companies-colorado/", "Why the Front Range is the right place to build this"),
    ("/about/", "About the company and the founder"),
]) + """
  </div>
</section>
""" + CTA_BAND

# ---------------------------------------------------------------- ABOUT
ABOUT_BODY = """
<section class="page-hero">
  <div class="wrap narrow">
    {crumbs}
    <div class="eyebrow">About</div>
    <h1>Standard SpaceWorX: an aerospace company in Loveland, Colorado</h1>
    <p class="lede">Standard SpaceWorX is a space debris removal venture of Standard Data Company. We design reusable servicing satellites, called Terriers, that capture orbital debris and return to a parked orbit for the next job. We are based in Loveland, Colorado, on the Front Range, and we serve satellite operators, government and defense buyers, aerospace partners, and investors across the United States.</p>
  </div>
</section>
<section class="article">
  <div class="wrap narrow prose">
    <h2>What we do</h2>
    <p>The company exists to make active debris removal a repeatable service. Everything else follows from that. We build vehicles that are reused rather than consumed, we lock each vehicle to one orbital plane and work that plane until it is clear, and we design the vehicle to earn imaging and hosted payload revenue between removals so a fleet can be financed before the removal market is fully priced. The vehicle is the <a href="/technology/terrier/">Terrier</a>. The reasoning is on the <a href="/mission/">mission page</a>.</p>

    <h2>Standard Data Company</h2>
    <p>Standard Data Company is a Loveland, Colorado S corporation. It is the parent of Standard SpaceWorX and holds all Standard SpaceWorX intellectual property, including the satellite design reference package and the patent landscape study. Standard Data Company also operates civic data infrastructure and custom software work, which is where the company's habit of publishing real numbers and building in the open comes from. Standard SpaceWorX is operated as a distinct venture with its own brand, channels, and investor relationships, and is structured so that it can be capitalized independently.</p>

    <h2>Leadership</h2>
    <h3 id="founder">Doug Mangeris, Founder and Chief Executive Officer</h3>
    <p>Doug Mangeris founded Standard SpaceWorX and leads it. His career is in field operations and large capital projects. As a commercial construction superintendent he has delivered more than 230 million dollars of work across healthcare, multifamily, senior living, retail, and industrial projects for general contractors including Hausmann Construction, Brinkmann Constructors, TCC Corporation, and Colorado Concepts. Before construction he spent four years in upstream oil and gas drilling with Cyclone Drilling, Helmerich and Payne, and Cade Drilling, and holds WellCAP master driller certification. He holds the ICC National Standard General Building Contractor (A) certification and MSHA and OSHA 40 hour certifications, and a bachelor's degree in History from the University of Nevada, Las Vegas.</p>
    <p>That background is deliberate for this company. Running a job site means sequencing crews, equipment, and materials so that expensive assets are never idle and every task follows a known procedure. A debris removal fleet is the same problem in a harder environment: a small number of expensive vehicles, a long list of targets, and a requirement that every capture follow a repeatable playbook. The Terrier program is run as a fleet operations problem with a hard engineering core.</p>
    <p>Doug serves as Vice President on the board of Habitat for Humanity of Loveland. He has a long-standing interest in civic accountability and data-driven decision making, which is reflected in how Standard SpaceWorX publishes its design reference values rather than keeping them vague.</p>

    <h2>How we work</h2>
    <ul>
      <li><strong>Numbers first.</strong> We publish our design reference values and the thresholds we are designing against, and we update them as the program matures.</li>
      <li><strong>Retire the hardest risk first.</strong> The capture of a tumbling, uncooperative object is the hardest step in the mission cycle, so it is the first thing we prototype, on the ground.</li>
      <li><strong>Standardize.</strong> A finite set of target classes, approach geometries, and capture procedures, so the fortieth mission costs less than the first.</li>
      <li><strong>Keep the sensors.</strong> Imaging on our vehicles is ours. Hosted payloads are transmit and receive hardware only.</li>
      <li><strong>Build domestic capability.</strong> We are a United States company operating from Colorado and we design for government and defense buyers who need a domestic removal option.</li>
    </ul>

    <h2>Where we are</h2>
    <p>Standard SpaceWorX operates from Loveland, Colorado, in Larimer County on the northern Front Range. Loveland sits between Fort Collins, home of Colorado State University, and the Boulder and Denver aerospace clusters, and within reach of the Space Force installations in Colorado Springs and Aurora. Colorado has one of the largest aerospace economies in the country, which is why the company is here: the propulsion, guidance, mechanisms, and operations talent the Terrier program needs lives within an hour's drive. We are a service-area business and do not operate a public walk-in office. Partners and investors are welcome to meet in Loveland, Fort Collins, Boulder, or Denver.</p>

    <h2>Who we serve</h2>
    <p>Satellite operators who need an object moved or a disposal partner. Government and defense buyers with catalog objects of concern. Aerospace partners in launch, propulsion, sensors, and ground operations. And investors who want exposure to on-orbit servicing through a model with recurring revenue. If that is you, the <a href="/contact/">contact page</a> is the fastest route to the founder.</p>

    <h2>Company facts</h2>
    <table>
      <tbody>
        <tr><th scope="row">Legal name</th><td>Standard SpaceWorX, a venture of Standard Data Company</td></tr>
        <tr><th scope="row">Parent</th><td>Standard Data Company, S corporation, Loveland, Colorado</td></tr>
        <tr><th scope="row">Founder and CEO</th><td>Doug Mangeris</td></tr>
        <tr><th scope="row">Headquarters</th><td>Loveland, Colorado, USA (service-area business)</td></tr>
        <tr><th scope="row">Sector</th><td>Aerospace; on-orbit servicing and active debris removal</td></tr>
        <tr><th scope="row">Contact</th><td><a href="mailto:contact@standardspaceworx.space">contact@standardspaceworx.space</a></td></tr>
        <tr><th scope="row">Website</th><td>https://standardspaceworx.space</td></tr>
      </tbody>
    </table>
""" + related([
    ("/technology/terrier/", "The Terrier reusable capture satellite"),
    ("/mission/", "Our mission"),
    ("/investors/", "Investor overview"),
    ("/news/", "News and updates"),
]) + """
  </div>
</section>
""" + CTA_BAND

# ---------------------------------------------------------------- CONTACT
CONTACT_BODY = """
<section class="page-hero">
  <div class="wrap">
    {crumbs}
    <div class="eyebrow">Contact</div>
    <h1>Contact Standard SpaceWorX</h1>
    <p class="lede">Investor, operator, government, and partner inquiries go directly to the founder. Use the form or email us. We respond to every serious inquiry.</p>
  </div>
</section>
<section>
  <div class="wrap contact-grid">
    <div>
      <form class="contact" action="https://formsubmit.co/StandardSpaceWorx@gmail.com" method="POST">
        <input type="hidden" name="_subject" value="Website inquiry: Standard SpaceWorX">
        <input type="hidden" name="_template" value="table">
        <input type="hidden" name="_captcha" value="false">
        <input type="hidden" name="_next" value="https://standardspaceworx.space/contact/thanks/">
        <input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
        <label>Name<input type="text" name="name" autocomplete="name" required></label>
        <label>Email<input type="email" name="email" autocomplete="email" required></label>
        <label>Organization<input type="text" name="organization" autocomplete="organization"></label>
        <label>Inquiry type
          <select name="inquiry_type" required>
            <option value="">Select one</option>
            <option>Investor</option>
            <option>Satellite operator</option>
            <option>Government or defense</option>
            <option>Aerospace partner or supplier</option>
            <option>Press</option>
            <option>Other</option>
          </select>
        </label>
        <label>Message<textarea name="message" required></textarea></label>
        <div><button class="btn solid" type="submit">Send inquiry</button></div>
      </form>
    </div>
    <div class="facts">
      <p><span class="k">Email</span><a href="mailto:contact@standardspaceworx.space">contact@standardspaceworx.space</a></p>
      <p><span class="k">Location</span>Loveland, Colorado, USA</p>
      <p><span class="k">Service area</span>Northern Colorado, the Front Range, and the United States</p>
      <p><span class="k">Hours</span>Monday to Friday, 8:00 AM to 5:00 PM Mountain</p>
      <p><span class="k">Investors</span>Put "Investor" in the inquiry type and tell us about your fund or strategic interest. See the <a href="/investors/">investor overview</a> first if you have not.</p>
      <p><span class="k">Operators and government</span>Tell us the object, the orbit, and the timeline. We will come back with what a Terrier can do and when.</p>
    </div>
  </div>
</section>
"""

THANKS_BODY = """
<section class="page-hero">
  <div class="wrap narrow">
    <div class="eyebrow">Contact</div>
    <h1>Inquiry received</h1>
    <p class="lede">Thank you. Your message is on its way to the founder. If it is urgent, email <a href="mailto:contact@standardspaceworx.space">contact@standardspaceworx.space</a> directly. In the meantime, the <a href="/technology/terrier/">Terrier program overview</a> and the <a href="/investors/">investor overview</a> cover most first questions.</p>
    <div class="cta-row"><a class="btn ghost" href="/">Back to the homepage</a></div>
  </div>
</section>
"""

# ---------------------------------------------------------------- NEWS INDEX
NEWS_BODY = """
<section class="page-hero">
  <div class="wrap narrow">
    {crumbs}
    <div class="eyebrow">News and updates</div>
    <h1>Space sustainability, debris policy, and the Terrier program</h1>
    <p class="lede">Written for satellite operators, investors, and government buyers who want the numbers behind the headlines. New posts are added as the program and the policy environment move.</p>
  </div>
</section>
<section>
  <div class="wrap narrow">
    <div class="posts">
      <article class="post">
        <div class="meta">2026-10-22 &middot; Orbital environment</div>
        <h2><a href="/news/kessler-syndrome-solutions/">Kessler syndrome solutions: what actually stabilizes low Earth orbit</a></h2>
        <p>Mitigation rules stop the problem from getting worse. Only removal of the largest objects makes it better. What the research says about how many, which ones, and why cost per object is the whole question.</p>
      </article>
      <article class="post">
        <div class="meta">2026-10-22 &middot; Policy</div>
        <h2><a href="/news/fcc-five-year-rule-orbital-debris-mitigation/">The FCC five year rule and the new economics of orbital debris mitigation</a></h2>
        <p>The rule, the first enforcement action, what ESA and insurers now require, and why compliance pressure creates a market for priced removal rather than funded demonstrations.</p>
      </article>
      <article class="post">
        <div class="meta">2026-10-22 &middot; Company</div>
        <h2><a href="/news/front-range-space-companies-colorado/">Why the Front Range is the right place to build a debris removal company</a></h2>
        <p>Colorado's aerospace economy, the Space Force footprint, the university pipeline, and what Northern Colorado specifically offers an early stage spacecraft company.</p>
      </article>
    </div>
  </div>
</section>
""" + CTA_BAND

# ---------------------------------------------------------------- POSTS
POST_KESSLER = """
<section class="page-hero">
  <div class="wrap narrow">
    {crumbs}
    <div class="meta">2026-10-22 &middot; Orbital environment &middot; Standard SpaceWorX</div>
    <h1>Kessler syndrome solutions: what actually stabilizes low Earth orbit</h1>
    <p class="lede">The Kessler syndrome is usually discussed as a doomsday scenario. It is better understood as a budgeting problem: a known number of objects need to come down each year, and the only open question is what each one costs.</p>
  </div>
</section>
<section class="article">
  <div class="wrap narrow prose">
    <h2>What the Kessler syndrome is</h2>
    <p>In 1978 Donald Kessler and Burton Cour-Palais of NASA published a paper showing that above a certain density of objects in low Earth orbit, collisions between those objects would generate fragments faster than atmospheric drag removed them. Each collision would raise the density, which would raise the collision rate, and the environment would degrade on its own even if no new satellites were launched. That cascade is what the term Kessler syndrome refers to.</p>
    <p>The important detail that gets lost in popular coverage is that the cascade is driven by mass, not by count. Small fragments are dangerous to individual satellites, but they do not create many new fragments when they hit something. Large derelicts do. A collision between two multi-tonne rocket bodies produces thousands of trackable fragments and far more that are too small to track. The future of the LEO environment is governed by a few thousand heavy objects, most of them dead satellites and spent upper stages that have been in orbit for decades.</p>

    <h2>Why mitigation alone does not solve it</h2>
    <p>Mitigation rules apply to new objects. The FCC's five year post-mission disposal rule, ESA's requirement for a 90 percent probability of successful disposal, and similar national guidelines all reduce the rate at which new derelicts are added. That matters, and the industry's compliance record is improving. But the heavy objects that drive the cascade are already in orbit. They were launched under rules that allowed 25 year disposal, or no disposal at all, and many of them are in orbits where natural decay takes centuries. Mitigation does not touch them. Modeling by NASA's Orbital Debris Program Office and others has consistently shown that even with full compliance on new launches and no further launches at all, the existing population in the most crowded altitude bands continues to grow through collisions.</p>

    <h2>What the research says stabilizes the environment</h2>
    <p>The same modeling work points to the solution. Studies from NASA, ESA, and the Inter-Agency Space Debris Coordination Committee over the last fifteen years converge on a figure: removing on the order of five to ten of the highest-risk large objects per year, selected by mass and collision probability, is enough to stabilize the LEO population when combined with mitigation on new launches. The exact number depends on the launch traffic assumed and the altitude band modeled, but the order of magnitude has been stable across studies and across agencies.</p>
    <p>Which objects matter most is also well characterized. The priority lists are dominated by a small number of object classes concentrated in a few orbital planes:</p>
    <ul>
      <li>The SL-16 (Zenit second stage) rocket bodies, eighteen of them at roughly 8,300 kg each, clustered near 840 km at 71 degrees inclination. A collision between any two would roughly double the tracked LEO debris catalog.</li>
      <li>Hundreds of SL-8 (Kosmos-3M upper stage) rocket bodies at roughly 1,400 kg each, between 780 and 980 km at 74 to 83 degrees inclination, many of them more than forty years old.</li>
      <li>Heavy derelict satellites in sun synchronous orbit near 98 degrees inclination, including Envisat at roughly 8,000 kg, along with the fragment cloud from the 2007 Fengyun-1C anti-satellite test, which remains the single largest debris-generating event in history.</li>
    </ul>
    <p>Three planes, an estimated 80 percent of the mass that matters. That concentration is good news. It means a removal campaign does not have to cover the whole sky. It has to work three job sites.</p>

    <h2>Why nothing has come down yet</h2>
    <p>If the number is five to ten per year and the targets are known, why has no uncooperative legacy object been removed? Cost. Every removal vehicle flown or contracted so far is single-use: it launches, captures one object, and deorbits with it. The entire program cost is charged to one removal, which lands in the 90 million dollar class per object. Ten removals a year at that price is close to a billion dollars a year, indefinitely. No operator, insurer, or government budget funds that as an operating expense, so removal has stayed a technology demonstration line funded by space agencies, and the demonstrations have been slow.</p>

    <h2>The solution is cost per object</h2>
    <p>The Kessler problem does not need a new physics breakthrough. It needs removal to cost what a compliance line item costs. That is a vehicle architecture question. A servicer that captures an object, disposes of it, and returns to a parked orbit for the next one spreads its vehicle, launch, and operations cost over dozens of removals. The Standard SpaceWorX <a href="/technology/terrier/">Terrier</a> is designed for up to 45 missions per tank of propellant, which moves the cost per object from the 90 million dollar class toward the 3 to 8 million dollar class. At that price, a ten object per year campaign is tens of millions, not a billion, and it can be paid for by the operators and insurers who benefit from a stable environment rather than by a single agency's research budget.</p>
    <p>Plane-locked operations make the economics better still. Because the priority mass sits in three planes, a vehicle assigned to one plane never pays the propellant cost of a plane change. It works its territory until the territory is clear, and in the sun synchronous plane it earns imaging and hosted payload revenue while it waits for the next tasking.</p>

    <h2>What operators and investors should take from this</h2>
    <ul>
      <li>The stabilization target is modest and well established: five to ten large objects per year.</li>
      <li>The targets are known and concentrated in three orbital planes.</li>
      <li>The barrier is cost per object, and cost per object is set by whether the vehicle is reused.</li>
      <li>Regulators and insurers are now creating the demand side. The <a href="/news/fcc-five-year-rule-orbital-debris-mitigation/">FCC five year rule post</a> covers that in detail.</li>
    </ul>
    <p>The <a href="/mission/">mission page</a> lays out why Standard SpaceWorX is built around reuse, and the <a href="/investors/">investor overview</a> covers how the program is sequenced.</p>
""" + related([
    ("/news/fcc-five-year-rule-orbital-debris-mitigation/", "The FCC five year rule and orbital debris mitigation"),
    ("/technology/terrier/", "The Terrier reusable capture satellite"),
    ("/mission/", "Why reusable beats single-use deorbit"),
    ("/news/", "All news and updates"),
]) + """
  </div>
</section>
""" + CTA_BAND

POST_FCC = """
<section class="page-hero">
  <div class="wrap narrow">
    {crumbs}
    <div class="meta">2026-10-22 &middot; Policy &middot; Standard SpaceWorX</div>
    <h1>The FCC five year rule and the new economics of orbital debris mitigation</h1>
    <p class="lede">For twenty years, orbital debris mitigation was a guideline. Between 2022 and 2026 it became a rule with an enforcement record, an insurance question, and a procurement requirement. That shift is what creates a market for priced debris removal.</p>
  </div>
</section>
<section class="article">
  <div class="wrap narrow prose">
    <h2>From 25 years to five</h2>
    <p>The long-standing international guideline for post-mission disposal in low Earth orbit was 25 years: a satellite should reenter or be moved to a disposal orbit within 25 years of the end of its mission. The guideline dated from an era of a few hundred active satellites, it was voluntary in most jurisdictions, and compliance was poor. Industry studies through the 2010s found that a large share of LEO payloads were not meeting it.</p>
    <p>In September 2022 the Federal Communications Commission adopted a rule shortening that window to five years for satellites operating below 2,000 km that are licensed by, or seek market access through, the FCC. Because the FCC licenses spectrum for nearly every commercial satellite that serves the United States market, the rule's reach extends well beyond American operators. The rule applies to satellites launched after a two year transition that ended in September 2024.</p>

    <h2>The first enforcement action</h2>
    <p>Rules change behavior when they are enforced. In October 2023 the FCC announced its first ever space debris enforcement action, a settlement with DISH Network over a geostationary satellite, EchoStar-7, that the operator had failed to move to the disposal orbit specified in its license because it ran short of propellant. The penalty was small, 150,000 dollars, but the precedent was not. The agency established that a disposal commitment in a license is an enforceable obligation and that it will act when one is missed. Every operator's regulatory counsel took note.</p>

    <h2>ESA, the Zero Debris approach, and the 90 percent requirement</h2>
    <p>The European Space Agency moved in parallel. ESA's updated space debris mitigation requirements call for a probability of successful disposal of at least 90 percent, a five year post-mission disposal window for LEO, and design features that make a failed satellite easier to remove. ESA has also pushed its Zero Debris approach, with a target that its own missions generate no new debris by 2030, and has invited industry to sign a Zero Debris Charter. Several national regulators and large operators have aligned with the five year window as well, which is turning it into a de facto global standard for new LEO systems.</p>

    <h2>Insurers have started asking</h2>
    <p>The space insurance market absorbed heavy losses in 2023 and has been more selective since. Underwriters now routinely ask about disposal reliability, propellant margins, and conjunction procedures before writing policies, and some are pricing debris risk into premiums for crowded altitude bands. For an operator, a credible disposal plan has become part of the cost of capital, not just a regulatory checkbox.</p>

    <h2>What mitigation does and does not do</h2>
    <p>All of the above applies to new satellites. It reduces the rate at which new derelicts accumulate, and it is necessary. It does nothing about the objects already in orbit that were launched under the 25 year guideline or before any guideline existed: the heavy rocket bodies and dead satellites that dominate the collision risk in the most crowded planes. Modeling consistently shows that even with perfect compliance on new launches, the existing population in those bands keeps growing through collisions unless the largest objects are actively removed. The <a href="/news/kessler-syndrome-solutions/">Kessler syndrome post</a> covers that research in detail.</p>

    <h2>Why compliance pressure creates a removal market</h2>
    <p>Here is the economic consequence. An operator who must guarantee 90 percent disposal reliability has a problem when a satellite fails in a way that prevents disposal. Under the old regime, that was a shrug. Under the new regime, it is a license violation, an insurance event, and a reputational issue with regulators the operator depends on for the next constellation approval. The operator would pay to have the object removed, if removal were available at a price that looked like an insurance premium rather than a space agency program.</p>
    <p>The same logic applies to anyone with a large investment in a specific orbital plane. Several gigawatt-scale orbital data center constellations have filed for sun synchronous orbit, the same band that holds the Fengyun-1C fragment cloud, Envisat, and other heavy legacy derelicts. An operator putting billions into that plane has a direct financial interest in the largest collision risks being removed before and during deployment, and a direct interest in a standing removal capability in the plane afterward.</p>
    <p>None of this creates demand for a 90 million dollar removal. All of it creates demand for a 3 to 8 million dollar one. That is the price point a reusable servicer reaches by spreading its vehicle, launch, and operations cost over dozens of removals, which is what the Standard SpaceWorX <a href="/technology/terrier/">Terrier</a> is designed to do.</p>

    <h2>What to watch next</h2>
    <ul>
      <li><strong>FCC rulemaking on orbital debris and in-space servicing.</strong> The agency has an open proceeding modernizing its rules for servicing, assembly, and manufacturing missions, which will shape how removal services are licensed.</li>
      <li><strong>Further enforcement.</strong> A second and third action, particularly against a LEO operator, will confirm that the five year rule is being policed.</li>
      <li><strong>Procurement language.</strong> Government buyers in the United States and Europe are beginning to write removal readiness and disposal reliability into contracts. That language is where a removal market becomes a line of business.</li>
      <li><strong>Insurance terms.</strong> Watch for explicit debris compliance conditions in policy language, which turn removal into a cost-avoidance decision an operator's finance team can evaluate.</li>
    </ul>
    <p>Standard SpaceWorX tracks these developments because they set the demand side of the Terrier program. The <a href="/investors/">investor overview</a> explains why the 2027 to 2030 window matters, and the <a href="/mission/">mission page</a> explains the vehicle architecture that meets it.</p>
""" + related([
    ("/news/kessler-syndrome-solutions/", "Kessler syndrome solutions that work"),
    ("/mission/", "Why reusable beats single-use deorbit"),
    ("/investors/", "Investor overview"),
    ("/news/", "All news and updates"),
]) + """
  </div>
</section>
""" + CTA_BAND

POST_COLORADO = """
<section class="page-hero">
  <div class="wrap narrow">
    {crumbs}
    <div class="meta">2026-10-22 &middot; Company &middot; Standard SpaceWorX</div>
    <h1>Why the Front Range is the right place to build a debris removal company</h1>
    <p class="lede">Standard SpaceWorX is based in Loveland, Colorado. That is not an accident of where the founder lives. It is where the talent, the customers, and the launch and operations partners for a reusable servicer program already are.</p>
  </div>
</section>
<section class="article">
  <div class="wrap narrow prose">
    <h2>Colorado's aerospace economy</h2>
    <p>Colorado has one of the largest aerospace economies in the United States and, by most measures, the largest per capita. The industry here spans the full stack: prime contractors building spacecraft and launch vehicles, satellite manufacturers and operators, Earth observation companies, component and propulsion suppliers, and the military space enterprise. Lockheed Martin Space is headquartered in the Denver suburbs. United Launch Alliance is based in Centennial. Boulder and Broomfield host major satellite and instrument manufacturers along with the Laboratory for Atmospheric and Space Physics at the University of Colorado, which has flown instruments on missions to every planet. Newer entrants in small satellite manufacturing, Earth observation, and in-space logistics have clustered in Denver, Westminster, Louisville, and Broomfield over the last decade.</p>

    <h2>The military and government footprint</h2>
    <p>Colorado Springs hosts United States Space Command and several Space Force installations, including Peterson and Schriever Space Force Bases. Buckley Space Force Base sits in Aurora on the east side of Denver. Space Operations Command and the units that track the orbital catalog and manage conjunction warnings are here. For a company whose product is removing objects from that catalog, and whose government and defense customers are the organizations that maintain it, being within a two hour drive of those buyers is a practical advantage, not a line on a slide.</p>

    <h2>The university pipeline</h2>
    <p>The University of Colorado Boulder runs one of the largest aerospace engineering programs in the country and has a long record of building and operating flight hardware through LASP. Colorado State University in Fort Collins, fifteen minutes from Loveland, produces mechanical, electrical, and systems engineers and has growing space and atmospheric science programs. The Colorado School of Mines in Golden is building a space resources program. Between them, the Front Range graduates spacecraft engineers every year, and a meaningful share of them want to stay in Colorado. For an early stage company whose first hires are propulsion, guidance and navigation, and mechanisms engineers, that pipeline is the single most important resource.</p>

    <h2>What Northern Colorado specifically offers</h2>
    <p>Loveland sits in Larimer County on the northern end of the Front Range, between Fort Collins and the Boulder and Denver clusters. Northern Colorado has an established precision manufacturing base, including aerospace component suppliers, and a cost of operating that is lower than Boulder or Denver while remaining within commuting distance of both. The Northern Colorado Regional Airport is in Loveland. For a company that will build and test ground prototype hardware before it builds flight units, access to machine shops, test facilities, and engineers who want to live near the mountains rather than in a metro core is a real advantage.</p>
    <p>Standard SpaceWorX is a service-area business. We do not operate a public walk-in office, and we meet partners and investors in Loveland, Fort Collins, Boulder, and Denver as needed. Our <a href="/about/">about page</a> has more on the company and the founder.</p>

    <h2>The Front Range space company landscape</h2>
    <p>The companies that make up Colorado's space economy are concentrated in a few corridors. The table below is a map of the ecosystem a Front Range space startup plugs into, not an exhaustive list.</p>
    <table>
      <thead><tr><th>Corridor</th><th>What is there</th><th>Why it matters to a servicer program</th></tr></thead>
      <tbody>
        <tr><td>Boulder and Broomfield</td><td>Satellite and instrument manufacturers, LASP, Earth observation and climate science</td><td>Sensors, flight software, imaging expertise for the Terrier's Earth observation revenue stream</td></tr>
        <tr><td>Denver, Centennial, Littleton</td><td>Prime contractors, launch vehicle operations, small satellite manufacturers</td><td>Bus components, launch integration, experienced systems engineers</td></tr>
        <tr><td>Westminster and Louisville</td><td>Earth observation operators, in-space logistics and habitat companies</td><td>Potential customers and partners for hosted payloads and on-orbit services</td></tr>
        <tr><td>Colorado Springs and Aurora</td><td>Space Command, Space Force bases, space domain awareness</td><td>Government and defense buyers, the orbital catalog, conjunction data</td></tr>
        <tr><td>Fort Collins and Loveland</td><td>Colorado State University, precision manufacturing, aerospace component suppliers</td><td>Engineering talent, prototype fabrication, lower operating cost</td></tr>
      </tbody>
    </table>

    <h2>Why this matters to investors</h2>
    <p>Location shows up in three places on a cap table. First, hiring: the engineers a prototype program needs are here and do not have to be relocated. Second, customer access: the government buyers who maintain the catalog and the commercial operators who need objects moved are within driving distance. Third, cost: Northern Colorado lets an early stage company run lean while staying inside the ecosystem. For investors looking at space startup investment in Colorado specifically, the Front Range is one of a small number of places in the country where a spacecraft company can be built end to end without leaving the state.</p>
    <p>The <a href="/investors/">investor overview</a> covers stage, roadmap, and how to reach the founder. The <a href="/technology/terrier/">Terrier page</a> covers what we are building here.</p>
""" + related([
    ("/investors/", "Investor overview"),
    ("/about/", "About Standard SpaceWorX"),
    ("/technology/terrier/", "The Terrier reusable capture satellite"),
    ("/news/", "All news and updates"),
]) + """
  </div>
</section>
""" + CTA_BAND


def _article_schema(path, headline, desc, published, section):
    return {
        "@context": "https://schema.org",
        "@type": "Article",
        "@id": SITE + path + "#article",
        "headline": headline,
        "description": desc,
        "url": SITE + path,
        "mainEntityOfPage": SITE + path,
        "datePublished": published + "T09:00:00-06:00",
        "dateModified": published + "T09:00:00-06:00",
        "articleSection": section,
        "inLanguage": "en-US",
        "image": SITE + "/assets/img/og-default.png",
        "author": {"@type": "Person", "@id": SITE + "/about/#founder", "name": ORG["founder"], "url": SITE + "/about/"},
        "publisher": {"@id": SITE + "/#organization"},
    }


def _service(sid, name, desc, url, stype):
    return {
        "@context": "https://schema.org",
        "@type": "Service",
        "@id": SITE + url + "#" + sid,
        "name": name,
        "serviceType": stype,
        "description": desc,
        "url": SITE + url,
        "provider": {"@id": SITE + "/#organization"},
        "areaServed": {"@type": "Country", "name": "United States"},
        "audience": {"@type": "BusinessAudience", "audienceType": "Satellite operators, government and defense buyers, aerospace partners, investors"},
    }


ADR_SERVICE = _service(
    "adr", "Active Debris Removal",
    "Capture and disposal of uncooperative orbital debris objects using reusable Terrier servicing satellites, priced per object rather than per vehicle.",
    "/mission/", "Active debris removal",
)
TERRIER_SERVICE = _service(
    "terrier-program", "Terrier Capture Program",
    "The Terrier program: a reusable servicing satellite that phases to a debris target, captures it, disposes of it, and returns to a parked orbit for up to 45 missions per tank.",
    "/technology/terrier/", "Reusable satellite servicing",
)

def org_schema():
    o = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "@id": SITE + "/#organization",
        "name": ORG["name"],
        "legalName": ORG["name"],
        "url": SITE + "/",
        "logo": {"@type": "ImageObject", "url": SITE + "/assets/img/logo-512.png", "width": 512, "height": 512},
        "image": SITE + "/assets/img/og-default.png",
        "description": ORG["description"],
        "email": ORG["email"],
        "foundingDate": ORG["foundingDate"],
        "founder": {"@type": "Person", "@id": SITE + "/about/#founder", "name": ORG["founder"], "jobTitle": "Founder and Chief Executive Officer", "url": SITE + "/about/"},
        "address": {"@type": "PostalAddress", "addressLocality": "Loveland", "addressRegion": "CO", "addressCountry": "US"},
        "areaServed": [{"@type": "Country", "name": "United States"}, {"@type": "State", "name": "Colorado"}],
        "parentOrganization": {"@type": "Organization", "name": ORG["parent"], "url": ORG["parentUrl"]},
        "knowsAbout": ["Active debris removal", "On-orbit servicing", "Space sustainability", "Orbital debris mitigation", "Sun synchronous orbit"],
        "contactPoint": [{"@type": "ContactPoint", "contactType": "sales", "email": ORG["email"], "areaServed": "US", "availableLanguage": "en"}],
    }
    if ORG.get("sameAs"):
        o["sameAs"] = ORG["sameAs"]
    return o


def website_schema():
    return {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "@id": SITE + "/#website",
        "url": SITE + "/",
        "name": ORG["name"],
        "publisher": {"@id": SITE + "/#organization"},
        "inLanguage": "en-US",
    }

PAGES = [
    {
        "path": "/",
        "title": "Standard SpaceWorX | Reusable Space Debris Removal Satellites",
        "description": "Standard SpaceWorX builds Terrier reusable satellites that capture orbital debris and return to a parked orbit for the next job. Loveland, Colorado.",
        "og_title": "Standard SpaceWorX | Reusable Space Debris Removal Satellites",
        "priority": "1.0",
        "changefreq": "weekly",
        "schemas": [org_schema(), website_schema(), ADR_SERVICE, TERRIER_SERVICE],
        "body": HOME_BODY,
    },
    {
        "path": "/technology/terrier/",
        "title": "Terrier Reusable Capture Satellite | Standard SpaceWorX",
        "description": "The Terrier is a reusable servicing satellite that phases to a debris target, captures it, disposes of it, and returns to park. Up to 45 missions per tank.",
        "og_image": "/assets/img/og-terrier.png",
        "og_alt": "Terrier reusable capture satellite mission cycle diagram with the Standard SpaceWorX wordmark",
        "priority": "0.9",
        "crumbs": [("/", "Home"), ("/technology/terrier/", "Technology"), ("/technology/terrier/", "Terrier")],
        "schemas": [TERRIER_SERVICE],
        "body": TERRIER_BODY,
    },
    {
        "path": "/mission/",
        "title": "Why Reusable Active Debris Removal | Standard SpaceWorX",
        "description": "Single-use deorbit vehicles die with their first target. Why reusable active debris removal is the only path to clearing low Earth orbit at scale.",
        "priority": "0.9",
        "crumbs": [("/", "Home"), ("/mission/", "Mission")],
        "schemas": [ADR_SERVICE],
        "body": MISSION_BODY,
    },
    {
        "path": "/investors/",
        "title": "Investors | Standard SpaceWorX Space Debris Removal",
        "description": "Investor overview for Standard SpaceWorX, a Colorado space startup building reusable debris removal satellites: stage, roadmap, and how to reach us.",
        "priority": "0.9",
        "crumbs": [("/", "Home"), ("/investors/", "Investors")],
        "body": INVESTORS_BODY,
    },
    {
        "path": "/about/",
        "title": "About Standard SpaceWorX | Aerospace Company, Loveland CO",
        "description": "Standard SpaceWorX is a Loveland, Colorado aerospace company founded by Doug Mangeris, under Standard Data Company, building reusable debris removal craft.",
        "priority": "0.8",
        "crumbs": [("/", "Home"), ("/about/", "About")],
        "schemas": [{
            "@context": "https://schema.org",
            "@type": "AboutPage",
            "@id": SITE + "/about/#page",
            "url": SITE + "/about/",
            "name": "About Standard SpaceWorX",
            "about": {"@id": SITE + "/#organization"},
            "mainEntity": {"@id": SITE + "/#organization"},
        }],
        "body": ABOUT_BODY,
    },
    {
        "path": "/news/",
        "title": "News and Updates | Standard SpaceWorX",
        "description": "Updates from Standard SpaceWorX on space sustainability, orbital debris policy, the Terrier program, and the Colorado space economy.",
        "priority": "0.7",
        "changefreq": "weekly",
        "crumbs": [("/", "Home"), ("/news/", "News")],
        "schemas": [{
            "@context": "https://schema.org",
            "@type": "CollectionPage",
            "@id": SITE + "/news/#page",
            "url": SITE + "/news/",
            "name": "News and Updates",
            "isPartOf": {"@id": SITE + "/#website"},
        }],
        "body": NEWS_BODY,
    },
    {
        "path": "/contact/",
        "title": "Contact Standard SpaceWorX | Loveland, Colorado",
        "description": "Contact Standard SpaceWorX in Loveland, Colorado. Investor, satellite operator, government, and partner inquiries reach the founder directly.",
        "priority": "0.8",
        "crumbs": [("/", "Home"), ("/contact/", "Contact")],
        "schemas": [{
            "@context": "https://schema.org",
            "@type": "ContactPage",
            "@id": SITE + "/contact/#page",
            "url": SITE + "/contact/",
            "name": "Contact Standard SpaceWorX",
            "mainEntity": {"@id": SITE + "/#organization"},
        }],
        "body": CONTACT_BODY,
    },
    {
        "path": "/contact/thanks/",
        "title": "Inquiry received | Standard SpaceWorX",
        "description": "Your inquiry to Standard SpaceWorX has been received.",
        "robots": "noindex,follow",
        "body": THANKS_BODY,
    },
]

POSTS = [
    {
        "path": "/news/kessler-syndrome-solutions/",
        "title": "Kessler Syndrome Solutions That Work | Standard SpaceWorX",
        "description": "What stabilizes low Earth orbit: removing five to ten large objects a year. Why mitigation alone is not enough and why cost per object is the real barrier.",
        "og_type": "article",
        "article": {"published": "2026-10-22", "section": "Orbital environment"},
        "lastmod": "2026-10-22",
        "crumbs": [("/", "Home"), ("/news/", "News"), ("/news/kessler-syndrome-solutions/", "Kessler syndrome solutions")],
        "schemas": [_article_schema("/news/kessler-syndrome-solutions/", "Kessler syndrome solutions: what actually stabilizes low Earth orbit", "What the research says actually stabilizes low Earth orbit: remove five to ten large objects a year. Why mitigation is not enough and cost per object is the barrier.", "2026-10-22", "Orbital environment")],
        "body": POST_KESSLER,
    },
    {
        "path": "/news/fcc-five-year-rule-orbital-debris-mitigation/",
        "title": "FCC 5-Year Rule and LEO Debris | Standard SpaceWorX",
        "description": "The FCC five year disposal rule, the first enforcement action, ESA's 90 percent rule, and why mitigation pressure creates a market for priced removal.",
        "og_type": "article",
        "article": {"published": "2026-10-22", "section": "Policy"},
        "lastmod": "2026-10-22",
        "crumbs": [("/", "Home"), ("/news/", "News"), ("/news/fcc-five-year-rule-orbital-debris-mitigation/", "FCC five year rule")],
        "schemas": [_article_schema("/news/fcc-five-year-rule-orbital-debris-mitigation/", "The FCC five year rule and the new economics of orbital debris mitigation", "The FCC five year disposal rule, the first enforcement action, ESA's 90 percent requirement, and why orbital debris mitigation pressure creates a market for priced removal.", "2026-10-22", "Policy")],
        "body": POST_FCC,
    },
    {
        "path": "/news/front-range-space-companies-colorado/",
        "title": "Front Range Space Companies, Colorado | Standard SpaceWorX",
        "description": "Why Standard SpaceWorX builds in Loveland: Colorado's aerospace economy, the Space Force footprint, the university pipeline, and Northern Colorado.",
        "og_type": "article",
        "article": {"published": "2026-10-22", "section": "Company"},
        "lastmod": "2026-10-22",
        "crumbs": [("/", "Home"), ("/news/", "News"), ("/news/front-range-space-companies-colorado/", "Front Range space companies")],
        "schemas": [_article_schema("/news/front-range-space-companies-colorado/", "Why the Front Range is the right place to build a debris removal company", "Why Standard SpaceWorX builds in Loveland: Colorado's aerospace economy, the Space Force footprint, the university pipeline, and Northern Colorado.", "2026-10-22", "Company")],
        "body": POST_COLORADO,
    },
]
