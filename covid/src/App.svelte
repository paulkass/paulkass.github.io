<script>
    import Chart from 'svelte-frappe-charts';

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

    let iso = 0;

    $: data = buildData(age, r_factor);

</script>

<h1>Will I get infected?</h1>

<form>
    <label>What is your age?</label>
    <input bind:value={age} placeholder="Enter your age"/>

    <!-- 
    <label>What state do you live in?</label>
    <select bind:value={iso} >
        {#each }

        {/each}
    </select>
    -->

    <label>What do you think the R-factor is in your area?</label>
    <input bind:value={r_factor} placeholder="1.0" type="number" />
</form>

<Chart data={data} type="percentage" />
