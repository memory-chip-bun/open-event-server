"""empty message

Revision ID: 0223c881d135
Revises: d1c2b8711223
Create Date: 2019-12-04 00:37:24.171728

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '0223c881d135'
down_revision = 'd1c2b8711223'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('name_event_deleted_at_uc', 'tickets', ['name', 'event_id', 'deleted_at'])
    op.drop_constraint('name_event_uc', 'tickets', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('name_event_uc', 'tickets', ['name', 'event_id'])
    op.drop_constraint('name_event_deleted_at_uc', 'tickets', type_='unique')
    # ### end Alembic commands ###
