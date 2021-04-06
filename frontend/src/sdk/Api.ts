import { AxiosInstance } from "axios";
import { LocalStorage, SessionStorage } from "quasar";
import { AccessToken } from "./Model";

declare module 'axios' {
    interface AxiosRequestConfig {
        dontWithJwt?: boolean
    }
}
export default class Api {
    axios: AxiosInstance

    constructor(axios: AxiosInstance, baseURL: string) {
        this.axios = axios
        this.axios.interceptors.request.use(config => {
            config.baseURL = baseURL
            if (!config.dontWithJwt) {
                let t: AccessToken = <AccessToken>LocalStorage.getItem('token')

                if (t == null || t.jwt == null)
                    throw new Error("Token is null!")
                if (t.expired_at != null && new Date() > t.expired_at)
                    throw new Error("Token exipred!")

                config.headers.Authorization = `Bearer ${t.jwt}`
            }
            return config
        }, err => Promise.reject(err))
    }

    async getToken(code: string, redirect_uri: string, client_id: string, client_secret: string): Promise<AccessToken> {
        const res = await this.axios.get("/token", {
            dontWithJwt: true,
            params: {
                code: code,
                redirect_uri: redirect_uri,
                client_id: client_id,
                client_secret: client_secret
            }
        });
        let token: AccessToken = <AccessToken>res.data;
        LocalStorage.set("token", token);
        return token;
    }

    async getUser(uid?: any): Promise<any> {
        const res = await this.axios.get("/user", {
            params: {
                "uid": uid
            }
        });
        let user = res.data;
        if (uid == null)
            SessionStorage.set("user", user);
        return user;
    }

    async processCommentTask(id: any, limit?: Number): Promise<any> {
        const res = await this.axios.post("/task/comment", {
            id: id,
            limit: limit
        });
        return res.data;
    }

    async getTimeline(page: Number): Promise<any> {
        const res = await this.axios.get("/timeline", {
            params: {
                page: page
            }
        });
        return res.data;
    }
}