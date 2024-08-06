<script>
    import { link } from "svelte-routing";
    
    import Logo from "../components/logo.svelte"
</script>

<main>
	<div class="logo-container">
		<Logo />
		<p class="common-font subtitle">- Song Recommendations Powered by Machine Learning -</p>
		<div class="buttons-container">
            <a href="/find" use:link>
                <button class="common-font try-it-out-btn">Try It Out!</button>
            </a>
			<a class="common-font github-btn" href="https://github.com/Alonkopilov" target="_blank">
				<img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="Icon">
				@alonkopilov
			</a>
		</div>
	</div>
</main>

<style>
	.logo-container {
		margin: 0;
		display: flex;
		align-items: center;
		justify-content: center;
		flex-direction: column;
		height: 100vh;
	}

	.github-btn {
		padding: 0.4em;
		gap: 0.5rem;
		display: flex;
		align-items: center;
		justify-content: center;
		border-radius: 5px;
		background-color: #373A40;
		font-size: 1rem;
		color: #ffffff;
		width: 10rem;
		text-decoration: none;
		text-align: center;
		cursor: pointer;
		height: 2.8rem;
		margin-bottom: 0.9em;
		border-width: 2px;
		border-color: white;
	}

	.github-btn img {
		filter: brightness(0) invert(1);
		width: 1.5rem;
		height: 1.5rem;
	}
	
	.try-it-out-btn:hover, .try-it-out-btn:focus, .try-it-out-btn:active {
		background-color: #ff4408;
	}
	.try-it-out-btn {
		border-radius: 5px;
		border-color: #ff4408;
		background-color: transparent;
		color: #e9e9e9;
		border-width: 2px;
		font-size: 1.5rem;
		width: 17rem;
		cursor: pointer;

		-webkit-transition-duration: 0.2s;
		transition-duration: 0.2s;
		-webkit-transition-property: color, background-color;
		transition-property: color, background-color;
	}
	
	.buttons-container {
		display: flex;
		align-items: center;
		justify-content: center;
		gap: 1rem;
		padding-top: 1rem;
	}

	.common-font {
		font-family: "Montserrat", sans-serif;
		font-optical-sizing: auto;
		font-weight: 700;
		font-style: normal;
		src: url("https://fonts.googleapis.com/css2?family=Montserrat:wght@700&display=swap");
		
	}

	.subtitle {
		font-size: 1.5rem;
		color: #ffffff;
	}

	:global(body) {
		/* background-color: #1c1c1e; */
		background: linear-gradient(-45deg, #313135, #1c1c1e);
		background-size: 400% 400%;
		animation: gradient 30s ease infinite;
	}

	@keyframes gradient {
		0% {
			background-position: 0% 50%;
		}
		50% {
			background-position: 100% 50%;
		}
		100% {
			background-position: 0% 50%;
		}
	}

	/* @media (min-width: 640px) {
		main {
			max-width: none;
		}
	} */
</style>