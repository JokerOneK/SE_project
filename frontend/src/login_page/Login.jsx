import React from 'react'
import { TextField, Button, Stack } from "@mui/material";
import { useForm } from 'react-hook-form';
import { yupResolver } from '@hookform/resolvers/yup';
import * as yup from 'yup';
import { NavLink } from 'react-router-dom'
const schema = yup
    .object()
    .shape({
        username: yup.string().required(),
        password: yup.string().min(8).required(),
    })
    .required();



export default function Login() {


    const { register, handleSubmit, formState: { errors }, setError } = useForm({
        resolver: yupResolver(schema),
    });

    const onSubmit = (data) => {

    }

    return (
        <>
            <Stack spacing={2}>
                <TextField error={!!errors.username?.message} helperText={errors.username?.message} {...register("username", { required: true })} label="Username" variant="standard" />
                <TextField error={!!errors.password?.message} helperText={errors.password?.message} {...register("password", { required: true })} label="Password" variant="standard" />

                <Button onClick={handleSubmit(onSubmit) } variant="contained">Login</Button>
                <Button variant="text"><NavLink to='/' style={isActive => ({
                    color: isActive ? "green" : "blue"
                    })}   >Register</NavLink>
                </Button>



            </Stack>


        </>
    )
}
