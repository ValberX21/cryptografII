document.querySelector('.encrpII').addEventListener('click', function(){
    let input = document.querySelector('.textUser').value;
    encryp(input);
})

function encryp(inputUser){
    const xhr = new XMLHttpRequest();
    //Create your API and put the link (endpoint) here
    xhr.open("GET",`?description=${inputUser}`);
    xhr.send();
    xhr.onload = function(){
        var data = JSON.parse(xhr.responseText)
        document.querySelector('.ecrypResult').textContent = data;               
    }
}