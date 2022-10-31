import React from 'react'
import { TextField, Button, Stack } from "@mui/material";
import { useForm } from 'react-hook-form';
import { yupResolver } from '@hookform/resolvers/yup';
import * as yup from 'yup';
import { NavLink } from 'react-router-dom'
import { useContext } from "react";
import AuthContext from "../context/AuthContext";


// const schema = yup
//     .object()
//     .shape({
//         username: yup.string().required(),
//         password: yup.string().min(8).required(),
//     })
//     .required();



export default function Login() {
    const { loginUser } = useContext(AuthContext);

    // const {register, formState: {errors}, setError} = useForm({
    //     resolver: yupResolver(schema),
    // });



    const handleSubmit = e => {
        e.preventDefault();
        const username = e.target.username.value;
        const password = e.target.password.value;
        username.length > 0 && loginUser(username, password);
    }

    return (
        <section>
            <form onSubmit={handleSubmit}>
                <h1>Login </h1>
                <hr />
                <label htmlFor="username">Username</label>
                <input type="text" id="username" placeholder="Enter Username" />
                <label htmlFor="password">Password</label>
                <input type="password" id="password" placeholder="Enter Password" />
                <button type="submit">Login</button>
            </form>
        </section>
            // <Stack spacing={2}>
            //     <form onSubmit={handleSubmit}>
            //     <TextField error={!!errors.username?.message}
            //                helperText={errors.username?.message} {...register("username", {required: true})}
            //                label="Username" variant="standard"/>
            //     <TextField error={!!errors.password?.message}
            //                helperText={errors.password?.message} {...register("password", {required: true})}
            //                label="Password" variant="standard"/>
            //
            //     <Button variant="contained">Login</Button>
            //     {/*<Button variant="text"><NavLink to='/' style={isActive => ({*/}
            //     {/*    color: isActive ? "green" : "blue"*/}
            //     {/*    })}   >Register</NavLink>*/}
            //     {/*</Button>*/}
            //     </form>
            //
            // </Stack>



        )
    }

