import Component from '@glimmer/component';
import { action } from '@ember/object';

export default class MeetingFormComponent extends Component {
  @action updateDate(arg) {
    let [date] = arg;
    let meeting = this.args.meeting;
    meeting.start_time = date;
  }

  @action submit() {
    this.args.submit();
  }
}
