<script>
    import Chart from 'svelte-frappe-charts';

    // Constants
    let countries = [ ["BE", "Belgium"], ["DE", "Germany"], ["FI", "Finland"], ["IT", "Italy"], ["LU", "Luxembourg"], ["NL", "Netherlands"], ["PL", "Poland"], ["UK", "United Kingdom"] ];

    // Functions
    function buildData(age, r_factor) {
        

        return {
            labels: ["Shop", "Work", "School"],
            datasets: [
            {
                name: "Results",
                values: [25, 50, 25]
            }
            ]
        };
    }

    // Parameters
    let age = 25;
    let r_factor = 1.0;
    let country = "UK";

    let iso = 0;

    $: data = buildData(age, r_factor);

</script>

<h1>Will I get infected?</h1>

<form>
    <label>What is your age?</label>
    <input bind:value={age} />

    <!-- 
    <label>What state do you live in?</label>
    <select bind:value={iso} >
        {#each }

        {/each}
    </select>
    -->

    <label>What do you think the R-factor is in your area?</label>
    <input bind:value={r_factor} type="number" />

    <label>What country do you think most closely reflects contact patterns in your area?</label>
    <select bind:value={country}>
        {#each countries as c}
        <option value={c[0]}>{c[1]}</option>
        {/each}
    </select>
</form>

<Chart data={data} type="percentage" />
