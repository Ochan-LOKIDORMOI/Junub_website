// Write code that filters the operations listed according to user input ass soon as they start typing on the search box
// It will be implemented inside the html document

function search() {
    const operations = document.getElementsByClassName('op');
    const search = document.getElementsByName('searchQuery').values.toUpperCase();

    for (let i = 0; i < operations.length; i++) {
        var operation = operations[i]
        const text = operation.textContent || operation.innerText;
        if (text.toUpperCase().indexOf(filter) > -1) {
            operation.style.display = '';
        } else {
            operation.style.display = 'none';
        }
    }
}
