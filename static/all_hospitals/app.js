/**
 * search_hospitals - A search engine
 * It takes the string from the search box on the page and queries the database for
 * results matching the query.
 * If the string is empty, it returns all hospitals
 */
let search=document.getElementById('search')
let search_box = document.getElementById('search_box')
let search_matches = document.getElementById('search_matches')
search.addEventListener('keydown', (e)=>{if (e.key == 'Enter'){search_hospitals()}})
search.addEventListener('click', (e)=>{search_matches.style.display = 'block'})

function search_hospitals(arg=false){
	let url = '/hospitals/search'
	let search_pharse = ''
	if (arg==false){search_pharse = search.value}
	else{search_pharse=arg}
	fetch(url, {
		headers : {'Content-Type': 'application/json'},
		method: 'POST',
		body: JSON.stringify({'message': search_pharse})
	}).then((res)=>{
		return res.json()
	}).then((json)=>{
		let hospitals = json['hospitals']
		let results = document.getElementById('results')
		results.innerHTML = ''
		for (let i = 0; i < hospitals.length; i++){
			let current_hospital = hospitals[i]
			let hospital = document.createElement('div')
			let name = document.createElement('p')
			name.innerHTML = current_hospital['name']
			hospital.appendChild(name)
			hospital.className = 'hospital'
			hospital.onclick = ()=>{
				window.location.href = '/hospital/' + current_hospital['id']
			}
			results.appendChild(hospital)
		}
	})
}
function search_match(){
	let url = '/hospitals/search_match'
	let search_pharse = document.getElementById('search').value
	if (search_pharse == ''){search_matches.innerHTML='';return;}
	fetch(url, {
		headers : {'Content-Type': 'application/json'},
		method: 'POST',
		body: JSON.stringify({'message': search_pharse})
	}).then((res)=>{
		return res.json()
	}).then((json)=>{
		let response = json['matches']
		search_matches.innerHTML = ''
		for (i = 0; i < response.length; i++){
			let name = response[i][0]
			let location = response[i][0]
			let match = document.createElement('p')
			match.innerText = `${name} . Location - ${location}`
			match.addEventListener('click', (e)=>{search_hospitals(name); console.log(name)})
			search_matches.appendChild(match)
		}
	})
}


search_hospitals()//Fill the initial page
