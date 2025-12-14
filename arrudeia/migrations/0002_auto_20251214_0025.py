# Generated manually to fix table name

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arrudeia', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            # Renomear a tabela de arrudeia_usuario para usuarios
            sql="ALTER TABLE arrudeia_usuario RENAME TO usuarios;",
            reverse_sql="ALTER TABLE usuarios RENAME TO arrudeia_usuario;",
        ),
    ]
