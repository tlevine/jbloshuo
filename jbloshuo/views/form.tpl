<h1>Hire a {{category_pretty}}</h1>
<form>
  <label name="description">{{description_label}}</label>
  <textarea placeholder="Write about the job, or provide a link to a description."
            name="description"></textarea>

  <label name="pay">{{pay_label}}</label>
  <select name="pay">
    % for option, pretty_option in pay_options:
    <option value="{{option}}">{{pretty_option}}</option>
    % end
  </select>

  <label name="initiative">{{initiative_label}}</label>
  <input type="text" name="initiative" />

  <input type="submit" name="kind" value="{{category}}" />
</form>
