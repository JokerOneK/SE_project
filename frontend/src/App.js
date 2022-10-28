import React, { useState } from 'react'
import './App.css';
import Todo from './TODO/Todo';
import Register from './registration page/Registration';
import Login from './login_page/Login';
import { BrowserRouter, Route, Routes,Link } from 'react-router-dom';
function App() {


  return (
    <div className="App">
      <img src='https://www.todo.de/assets/todo-logo.png' className='todoImage'/>
      <BrowserRouter>
        <Routes>
          <Route path='/login' element={<Login />}/>
          <Route path='/todo' element={<Todo />}/>
          <Route path='/' element={<Register />}/>
        </Routes>
      </BrowserRouter>

    </div>
  );
}

export default App;
