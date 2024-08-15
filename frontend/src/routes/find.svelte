<script>
    import { link } from "svelte-routing";

    import Logo from "../components/logo.svelte"
    import Song from "../components/song.svelte";

    var API_IP = "localhost"
    var API_PORT = 4000
    var BACKEND_API_URL = `http://${API_IP}:${API_PORT}`
    var SPOTIFY_API_URL = `https://accounts.spotify.com`

    // Search Related Functions
    async function fetchSongs(query) {
        console.log(`THIS = ${API_IP}, ${API_PORT}`)
        var findMeSongsApiEndpoint = `${BACKEND_API_URL}/search`
        try {
            const params = new URLSearchParams({
                'query': query
            })

            const response = await fetch(`${findMeSongsApiEndpoint}/?${params.toString()}`)

            data = await response.json()
            options = data["result"]
        } catch (err) {
            error = err.message;
            console.log(`[fetchSongs] ERROR: ${error}`)
        } finally {
            loading = false
        }
    }

    function debounce(func, wait) {
        let timeout;

        return function(...args) {
            clearTimeout(timeout);
            timeout = setTimeout(() => func.apply(this, args), wait)
        };
    }

    const debouncedSearchSongs = debounce(fetchSongs, 300);

    function handleInput(e) {
        let searchQuery = e.target.value

        debouncedSearchSongs(searchQuery)
    }

    // Generate Similar Songs Related Functions
    let featureSong = "";
    let similarSongs = []

    async function requestSimilarSongs() {
        var findMeSongsApiEndpoint = `${BACKEND_API_URL}/find_songs`
        try {
            let songName = ""
            let songArtist = ""
            let amount = 10

            let songTitleParts = featureSong.split("-")
            songArtist = songTitleParts[0].trim()
            if (songTitleParts.length == 2) {
                songName = songTitleParts[1].trim()
            }
            
            const params = new URLSearchParams({
                'name': songName,
                'artist': songArtist,
                'amount': amount
            })

            const response = await fetch(`${findMeSongsApiEndpoint}/?${params.toString()}`)

            data = await response.json()
            
            let results = []
            data.forEach((song, index) => {
                results.push({
                    "track_id": song["track_id"]
                })
            });

            similarSongs = results

        } catch (err) {
            error = err.message;
            console.log(`[requestSimilarSongs] ERROR: ${error}`)
        } finally {
            loading = false
        }
    }

    let access_token = ""
    async function requestAccessToken() {
        var accessTokenApiEndpoint = `${SPOTIFY_API_URL}/api/token`
        try {            
            const body = new URLSearchParams({
                'grant_type': 'client_credentials',
                'client_id': process.env.VITE_SPOTIFY_API_CLIENT_ID,
                'client_secret': process.env.VITE_SPOTIFY_API_CLIENT_SECRET,
            })
            const headers = {
                'Content-Type': "application/x-www-form-urlencoded"
            }
            const response = await fetch(accessTokenApiEndpoint, {
                method: "POST",
                headers: headers,
                body: body
            })

            data = await response.json()
            
            access_token = data["access_token"]

        } catch (err) {
            error = err.message;
            console.log(`[requestAccessToken] ERROR: ${error}`)
        } finally {
            loading = false
        }
    }

    async function generateSimilarSongs() {
        requestAccessToken()
        requestSimilarSongs()
    }

    let data = null;
    let loading = true;
    let error = null;
    let options = []
</script>

<main>
    <div class="page-stucture">
        <div class="search-part-container">
            <div class="search-part">
                <div class="logo-container">
                    <a style="color: brown;" href="/" use:link replace>
                        <Logo />
                    </a>
                </div>
                <label for="search-songs" class="common-font enter-song-label">Recommend me songs based on:</label>
                <div class="search-songs-input-container">
                    <input on:input={handleInput} bind:value={featureSong} list="search-results-list" id="search-songs" type="text" class="search-songs">
                    <button on:click={generateSimilarSongs} class="go-search-btn">Go</button>
                </div>
                <datalist class="search-results-list" id="search-results-list">
                    {#each options as option}
                        <option value={option}>
                    {/each}
                </datalist>
            </div>
        </div>
        <div class="results-part">
            {#each similarSongs as similarSong (similarSong.track_id)}
                <Song song_spotify_id={similarSong.track_id} access_token_spotify={access_token}/>
            {/each}
        </div>
    </div>
    
</main>

<style>
    .search-results-list {
        height: 50rem;
    }
    .page-stucture {
        display: flex;
    }

    .search-part-container {
        width: 25%;
    }

    .results-part {
        margin-top: 4rem;
        width: 75%;
        gap: 5rem;
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        justify-content: flex-start;
        margin-bottom: 4rem;
    }

    .go-search-btn:hover, .go-search-btn:focus, .go-search-btn:active {
		background-color: #ff4408;
	}
	.go-search-btn {
		border-radius: 5px;
		border-color: #ff4408;
		background-color: transparent;
		color: #e9e9e9;
		border-width: 2px;
		cursor: pointer;
        width: 4rem;

		-webkit-transition-duration: 0.2s;
		transition-duration: 0.2s;
		-webkit-transition-property: color, background-color;
		transition-property: color, background-color;
	}

    .search-songs-input-container {
        display: flex;
        flex-direction: row;
        gap: 0.5rem;
    }

    .enter-song-label {
        color: white;
        margin-top: -2.5rem;
        margin-bottom: 0.5rem;
    }

    .common-font {
		font-family: "Montserrat", sans-serif;
		font-optical-sizing: auto;
		font-weight: 400;
		font-style: normal;
		src: url("https://fonts.googleapis.com/css2?family=Montserrat:wght@400&display=swap");
	}

    .search-songs {
        width: 17rem;
    }

    .search-part {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin: 0;
    }

    .logo-container {

        scale: 0.5;
    }
    
</style>