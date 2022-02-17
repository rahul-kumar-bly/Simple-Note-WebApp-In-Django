
// alternate background for note list main page
    const listItems = document.getElementById('article-list').querySelectorAll('h1')
    for (let i = 0; i<= listItems.length;i++){
        if (i%2 === 0){
            listItems[i].className = "newh1"
        }
    };
