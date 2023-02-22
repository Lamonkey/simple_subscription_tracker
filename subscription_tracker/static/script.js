const base_url = "http://127.0.0.1:5000/"

console.log("added")

//log passed parameter when onclick is called
const handleSubmission = (data) => {
    event.preventDefault();
    
    const name = document.getElementById('name').value;
    const tag = document.getElementById('tag').value;
    const date = document.getElementById('date').value;
    const price = document.getElementById('price').value;

    // do something with the form data
    console.log(name, tag, date, price);
    //post data to server
    fetch(base_url + "add", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            name: name,
            tag: tag,
            date: date,
            price: price,
        }),
    })
        .then((response) => response.json())
        .then((data) => {
            console.log("Success:", data);
        }
        )
        .catch((error) => {
            console.error("Error:", error);
        }
        );
        
}

  
document.getElementById("submit-btn").onclick = handleSubmission;
