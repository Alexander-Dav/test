from flask_admin.contrib.sqla import ModelView
from wtforms import SelectField, IntegerField
from wtforms.validators import Optional

class TestView(ModelView):
    form_extra_fields = {
        'timer_seconds': IntegerField('Время (сек)', validators=[Optional()])
    }
    
    form_choices = {
        'topic_id': [(t.id, t.name) for t in Topic.query.all()]
    }

    def on_model_change(self, form, model):
        model.timer_enabled = bool(form.timer_seconds.data)

    def delete_model(self, model):
        if TestResult.query.filter_by(test_id=model.id).count() > 0:
            flash('Нельзя удалить тест с результатами', 'danger')
            return False
        return super().delete_model(model)