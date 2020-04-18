import Route from '@ember/routing/route';

export default class MeetingsNewRoute extends Route {
  model() {
    return this.store.createRecord('meeting');
  }
}
