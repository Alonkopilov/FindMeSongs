<script>
	import { Router, Route } from "svelte-routing";

	import HomePage from "./routes/home.svelte";
	import FindPage from "./routes/find.svelte";

	export let url = "/"
</script>

<Router {url}>
	<div>
		<Route path="/" component={HomePage} />
		<Route path="/find" component={FindPage} />
	</div>
</Router>