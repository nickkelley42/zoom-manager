import Controller from '@ember/controller';
import { action } from '@ember/object';

export default class MeetingsNewController extends Controller {
  @action submit() {
    let meeting = this.get('model');
    this.set('message', '...');
    meeting.save().then(() => {
      this.transitionToRoute('meetings.index');
    });
  }
}
