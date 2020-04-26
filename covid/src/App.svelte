<script>
    import Chart from 'svelte-frappe-charts';

    let data = {
        labels: ["Shop", "School", "Work"],

        datasets: [
            { name: "Some Data", values: [25, 50, 25] }
        ]
    };

</script>

<h1>Will I get infected?</h1>

<Chart data={data} type="percentage" />
