import AuthOnlyRoute from "./auth-only-route";

export default class PreferencesRoute extends AuthOnlyRoute {
  model() {
    return {};
  }
}
