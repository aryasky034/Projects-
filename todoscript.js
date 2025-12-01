// Get elements
const input = document.getElementById("todo-input");
const addBtn = document.getElementById("add-btn");
const list = document.getElementById("todo-list");

// Load saved todos from localStorage on page load
let todos = JSON.parse(localStorage.getItem("todos")) || [];
renderList();

// Add item
addBtn.addEventListener("click", addTodo);
input.addEventListener("keyup", function (e) {
  if (e.key === "Enter") addTodo();
});

function addTodo() {
  const text = input.value.trim();
  if (!text) return;

  // Add to array
  todos.push(text);
  // Save to localStorage
  localStorage.setItem("todos", JSON.stringify(todos));

  // Update UI
  renderList();
  input.value = "";
}
 
// Remove item by index
function removeTodo(index) {
  todos.splice(index, 1);                     // remove from array
  localStorage.setItem("todos", JSON.stringify(todos)); // update storage
  renderList();                               // re-render UI
}

// Render list from todos array
function renderList() {
  list.innerHTML = ""; // clear old list

  todos.forEach((todoText, index) => {
    const li = document.createElement("li");
    li.textContent = todoText;

    const delBtn = document.createElement("button");
    delBtn.textContent = "X";
    delBtn.style.marginLeft = "8px";

    // On click, remove this item
    delBtn.addEventListener("click", function () {
      removeTodo(index);
    });

    li.appendChild(delBtn);
    list.appendChild(li);
  });
}
