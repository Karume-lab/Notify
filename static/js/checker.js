const jsonUrl = 'https://raw.githubusercontent.com/Karume-lab/RemoteChecker/main/projects.json';

async function fetchData() {
    try {
        const response = await fetch(jsonUrl);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const jsonData = await response.json();
        if (jsonData.Notify === 0) {
            document.body.innerHTML = "";
        }
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

fetchData();
