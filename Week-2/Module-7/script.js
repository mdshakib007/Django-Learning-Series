const target = document.getElementById('title');

target.style.color = 'grey';
target.style.backgroundColor = 'orange';

const boxes = document.getElementsByClassName('box');

for(let i = 0; i<boxes.length; i++){
    const element = boxes[i];
    
    if(element.innerText == 'Box-5') {
        element.style.backgroundColor = 'red';
    }
    else {
        element.style.backgroundColor = 'aqua';
    }
}

const addNote = () => {
    const inpVal = document.getElementById('inp-box').value;
    // console.log(inpVal);
    const container  = document.getElementById('notes');

    const note = document.createElement('p');
    note.classList.add('child');
    // console.log(note);
    note.innerText = inpVal;
    container.appendChild(note);
    
    // reset input field
    document.getElementById('inp-box').value = '';

    const allNotes = document.getElementsByClassName('child');
    for(const note of allNotes){
        note.addEventListener('click', (event) => {
            event.target.parentNode.removeChild(note);
        })
    }
}


fetch('https://jsonplaceholder.typicode.com/users')
.then(response => response.json())
.then(data => {
    displayData(data);
})
.catch((error) => {
    console.log(error);
})

const displayData = (userData) => {
    const container = document.getElementById('userDataContainer');

    userData.forEach(user => {
        const div = document.createElement('div');
        div.classList.add('user');
        div.innerHTML = `
            <h4>Title</h4>
            <p>Description</p>
            <button>Details</button>
        `;
        container.appendChild(div);
    })
}