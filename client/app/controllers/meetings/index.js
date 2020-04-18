import Controller from '@ember/controller';

export default class MeetingsIndexController extends Controller {
  get hasMeetings() {
    return this.get('model.length') > 0;
  }
}
