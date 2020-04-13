import AuthOnlyRoute from "./auth-only-route";

export default class MeetingsRoute extends AuthOnlyRoute {
  model() {
//    return this.store.findAll("meeting");
    return [];
  }
}
