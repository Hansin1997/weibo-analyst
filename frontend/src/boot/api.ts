import axios from 'axios';
import { env } from 'process';
import { boot } from 'quasar/wrappers';
import Api from 'src/sdk/Api';

declare module 'vue/types/vue' {
    interface Vue {
        $api: Api;
    }
}

export default boot(({ Vue }) => {
    // eslint-disable-next-line @typescript-eslint/no-unsafe-member-access
    Vue.prototype.$api = new Api(axios.create(), env.API_URL || "http://127.0.0.1:5000");
});
