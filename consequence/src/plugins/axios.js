import axios from 'axios';

axios.defaults.baseURL = process.env.VUE_APP_API_URL + '/api/';
axios.defaults.headers.common["Content-Type"] = "application/json";

// Add a request interceptor
axios.interceptors.request.use(function (config) {
    // Do something before request is sent
    if (localStorage.getItem('userInfo'))
        config['headers']['Authorization'] = "Bearer " + JSON.parse(localStorage.getItem('userInfo')).access;

    return config;
}, function (error) {
    // Do something with request error
    return Promise.reject(error);
});

// Add a response interceptor
axios.interceptors.response.use(function (response) {
    // Any status code that lie within the range of 2xx cause this function to trigger
    // Do something with response data
    return response;
}, function (error) {
    // Any status codes that falls outside the range of 2xx cause this function to trigger
    // Do something with response error
    // console.log(error.response);
    if (error.response && error.response.status === 401 && error.response.data.code === "token_not_valid") {
        localStorage.removeItem('userInfo');
        alert('Session Expired, Please login again.');
        window.location.reload();
    }
    return Promise.reject(error);
});

export default axios;