import React, { useState } from 'react'
import MyInput from './myInput';
import Tasks from './Tasks';
import Sort from './Sort';
import Search from './Search';

function Todo(){
    const [array, setArray] = useState(JSON.parse(localStorage.getItem('todo')) || []);


    function deleteItem(itemDelete) {
      const i = array.filter((item) => item.id != itemDelete.id)
      setArray(i);
      local(i);
    }
    function local(xxx) {
      localStorage.setItem('todo', JSON.stringify(xxx));
    }
    function guidGenerator() {
      var S4 = function () {
        return (((1 + Math.random()) * 0x10000) | 0).toString(16).substring(1);
      };
      return (S4() + S4() + "-" + S4() + "-" + S4() + "-" + S4() + "-" + S4() + S4() + S4());
    }
    function AppAdd(item) {
      let newArray = [...array, { id: guidGenerator(), name: item }];
      setArray(newArray);
      local(newArray);
    }
    function deleteSelected(arr) {
      const numbers = [];
      for (let i = 0; i < arr.length; i++) {
        for (let j = 0; j < array.length; j++) {
          if (array[j].id == arr[i]) {
            numbers.push(j);
          }
        }
      }
      const arr2 = [];
      const numbers2 = [];
      for (let i = 0; i < array.length; i++) {
        if (!numbers.includes(i)) {
          numbers2.push(i);
        }
      }
      numbers2.map((index) => { arr2.push(array[index]) });
      setArray(arr2);
      local(arr2)
  
  
    }
    function deleteAll() {
      setArray([]);
      local([]);
    }
  
    function changingFunc(sort) {
      setSelectedSort(sort);
      setArray([...array].sort((a, b) => a[sort].localeCompare(b[sort])))
  
    }
    const [selectedSort, setSelectedSort] = useState('');
  
    const [searchQuery, setSearchQuery] = useState('');
    function getSortedByQuery() {
      return array.filter(elem => elem.name.toLowerCase().startsWith(searchQuery));
    }
    const sortedByQuery = getSortedByQuery();
    return(
        <div className="TODO">
      <MyInput addTask={AppAdd} />
      <div className='sorting'>
        <Sort className="sort-bar"
          value={selectedSort}
          onChangingFunc={changingFunc}
          defaultValue="Sorting"
          options={[
            { value: 'name', name: "By name" },
            { value: 'id', name: 'By ID number' }
          ]}
        />
        <Search className="search-bar" searchQuery={searchQuery} setSearchQuery={setSearchQuery} />

      </div>
      <Tasks className="listOfTodos" array={sortedByQuery} deleteTask={deleteItem} deleteSelected={deleteSelected} deleteAll={deleteAll} />
     </div>

    );
};


export default Todo;