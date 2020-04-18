import { helper } from '@ember/component/helper';

export default helper(function datetime(args) {
  let date = args[0];
  let ds = date.toLocaleDateString();
  let ts = date.toLocaleTimeString();
  return `${ds} ${ts}`;
});
