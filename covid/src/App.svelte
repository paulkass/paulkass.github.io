<script>
    import Chart from 'svelte-frappe-charts';

    // Constants
    let COUNTRIES = [ ["BE", "Belgium"], ["DE", "Germany"], ["FI", "Finland"], ["IT", "Italy"], ["LU", "Luxembourg"], ["NL", "Netherlands"], ["PL", "Poland"], ["UK", "United Kingdom"] ];
    let PLACES = ["Home", "Work", "School", "Transport", "Leisure", "Other"]; 
    let PLACE_MAPPINGS = {
        "Home": "cnt_home",
        "Work": "cnt_work",
        "School": "cnt_school",
        "Transport": "cnt_transport",
        "Leisure": "cnt_leisure",
        "Other": "cnt_otherplace"
    };
    let AGE_BUCKETS = [[0, 10], [11, 20], [21, 30], [31, 40], [41, 50], [51, 60], [61, 70], [80, 120]];
    let NAN_DATASET = {
            labels: [],
            datasets: []
    };

    var age_sorted_contacts = {};

    Papa.parse("data/2008_Mossong_POLYMOD_COMPUTED_contacts.csv", 
        {
            download: true,
            header: true,
            complete: function(results, file) {
                results = results.data;
                var result;
                for (result of results) {
                    let a = getAgeBucket(result.part_age);
                    if (!(a in age_sorted_contacts )) {
                        age_sorted_contacts[a] = []; 
                    }
                    age_sorted_contacts[a].push(result);
                }

                data = buildData(age, r_factor, country, places); 
            }
        }
        )


    // Functions
    function getAgeBucket(a) {
        var i;
        for (i of AGE_BUCKETS) {
            if (a >= i[0] && a <= i[1]) {
                return i;
            }
        }
    }

    function buildData(age, r_factor, country, places) {
        var relevant_results = age_sorted_contacts[getAgeBucket(age)]

        let trueFalseFunc = function(v) {
            if (v == "True") {
                return 1;
            } else {
                return 0;
            }
        };

        if (relevant_results == null) {
            console.log("results are empty");
            return NAN_DATASET;
        }

        relevant_results = relevant_results
        .filter(x => {
            return x.participant_nationality == country;
        })
        .map(function(x) {
            var r = {};
            for (p in PLACE_MAPPINGS) {
                r[p] = trueFalseFunc(x[PLACE_MAPPINGS[p]]);
            }
            return r;
        });

        if (relevant_results == null || relevant_results.length == 0) {
            alert("Data not available for this demographic");
            return NAN_DATASET;
        }

        relevant_results = relevant_results.reduce(function(x, y) {
            var r = {};
            for (p of PLACES) {
                r[p] = x[p] + y[p];
            }
            return r;
        });
        
        var ret = {};
        var p;
        for (p in relevant_results) {
            if (places.includes(p)) { 
                ret[p] = relevant_results[p];
            }
        }

        return {
            labels: Object.keys(ret),
            datasets: [
            {
                name: "Results",
                values: Object.values(ret) 
            }
            ]
        };
    }

    // Parameters
    var age = 25;
    var r_factor = 1.0;
    var country = "UK";
    var places = PLACES.slice();

    $: data = buildData(age, r_factor, country, places);

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
        {#each COUNTRIES as c}
        <option value={c[0]}>{c[1]}</option>
        {/each}
    </select>

    <label>Which of these locations do you visit?</label>
    
    {#each PLACES as p}
        <label>
            <input type=checkbox bind:group={places} value={p}>
            {p}
        </label>
    {/each}
</form>

<Chart data={data} type="percentage" />
