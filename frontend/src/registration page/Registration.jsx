import React from "react";
import { TextField, Button, Stack } from "@mui/material";
import './registration.css'
import { useForm } from 'react-hook-form';
import { yupResolver } from '@hookform/resolvers/yup';
import * as yup from 'yup';
import { NavLink } from "react-router-dom";
import axios from "axios";

const schema = yup
    .object()
    .shape({
        email: yup.string().required().email(),
        name: yup.string().required(),
        username: yup.string().required(),
        password: yup.string().min(8).required(),
    })
    .required();


function Register() {




    const { register, handleSubmit, formState: { errors } } = useForm({
        resolver: yupResolver(schema),
    });

    const onSubmit = (data) => {

        axios.post('localhost:3000', data)
            .then(function (response) {
                console.log(response);
            })
            .catch(function (error) {
                console.log(error);
            });
        console.log(data);

    }
    function goToLogin() {
        return NavLink


    }
    return (
        <Stack spacing={1}>
            <TextField error={!!errors.name?.message} helperText={errors.name?.message} {...register("name", { required: true })} label="First name" variant="standard" />
            {/* <TextField error={!!errors.lastname?.message} helperText={errors.lastname?.message} {...register("lastname", { required: true })} label="Last name" variant="standard" /> */}
            <TextField error={!!errors.email?.message} helperText={errors.email?.message} {...register("email", { required: true })} label="Email" variant="standard" />
            <TextField error={!!errors.username?.message} helperText={errors.username?.message} {...register("username", { required: true })} label="Username" variant="standard" />
            <TextField error={!!errors.password?.message} helperText={errors.password?.message} {...register("password", { required: true })} label="Password" variant="standard" />
            {/* <TextField error={!!errors.confirmPassword?.message} helperText={errors.confirmPassword?.message} {...register("confirmPassword", { required: true })} label="Confirm Password" variant="standard" /> */}


            <Button onClick={handleSubmit((onSubmit))} variant='contained'>
                Register
            </Button>
            <Button>
                <NavLink to='/login' style={isActive => ({
                    color: isActive ? "green" : "blue"
                })}   >Login
                </NavLink>
            </Button>
        </Stack>
    );

}


export default Register;