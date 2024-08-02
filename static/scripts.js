document.addEventListener('DOMContentLoaded', function () {
    const searchBox = document.getElementById('search-box');
    const viewAllButton = document.getElementById('view-all-button');
    const taskList = document.getElementById('task-list');
    const tasks = taskList.getElementsByClassName('task-item');

    searchBox.addEventListener('input', function () {
        const filter = searchBox.value.toLowerCase();

        Array.from(tasks).forEach(function (task) {
            const taskText = task.textContent.toLowerCase();
            if (taskText.includes(filter)) {
                task.style.display = '';
            } else {
                task.style.display = 'none';
            }
        });
    });

    searchBox.addEventListener('keypress', function (e) {
        if (e.key === 'Enter') {
            e.preventDefault();
        }
    });

    viewAllButton.addEventListener('click', function () {
        searchBox.value = '';
        Array.from(tasks).forEach(function (task) {
            task.style.display = '';
        });
    });
});