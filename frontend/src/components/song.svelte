<script>
    export let song_spotify_id = "";
    export let access_token_spotify = "";

    let loading = true;
    let error = null;
    let track_data = {}
    let track_name = ""
    let track_artist = ""
    let track_cover_url = ""
    let track_spotify_url = ""

    async function fetchTrackData(spotify_track_id, access_token) {
        var API_URL = `https://api.spotify.com`
        var fetchTrackApiEndpoint = `${API_URL}/v1/tracks/${spotify_track_id}`

        try {
            const headers = {
                "Authorization": `Bearer ${access_token}`,
                "Content-Type": 'application/json'
            }

            const response = await fetch(fetchTrackApiEndpoint, {
                method: 'GET',
                headers: headers
            })

            track_data = await response.json()

            track_name = track_data["name"]
            track_artist = track_data["artists"][0]["name"]
            track_cover_url = track_data["album"]["images"][0]["url"]
            track_spotify_url = track_data["external_urls"]["spotify"]
        } catch (err) {
            error = err.message;
            console.log(`[fetchTrackData] ERROR: ${error}`)
        } finally {
            loading = false
        }
    }

    console.log(`Fetching data for song ${song_spotify_id}`)
    fetchTrackData(song_spotify_id, access_token_spotify)
</script>

<main>
    <a href={track_spotify_url} target="_blank">
        <img class="card-img" src={track_cover_url} alt="cover">
    </a>
    <p class="common-font card-title">{track_name}</p>
    <p class="common-font card-subtitle">{track_artist}</p>
</main>

<style>
    .card-title {
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        max-width: 15rem;
        font-size: 1.7rem;
        margin: 0;
        color: #ffffff;
    }

    .card-subtitle {
        font-size: 1rem;
        margin: 0;
        color: #b9b9b9
    }

    .card-img {
        height: 15rem;
        width: 15rem;
    }

    .common-font {
		font-family: "Montserrat", sans-serif;
		font-optical-sizing: auto;
		font-weight: 700;
		font-style: normal;
		src: url("https://fonts.googleapis.com/css2?family=Montserrat:wght@700&display=swap");
	}
</style>