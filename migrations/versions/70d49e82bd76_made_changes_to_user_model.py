"""made changes to user model

Revision ID: 70d49e82bd76
Revises: 9193dfa10046
Create Date: 2019-12-10 04:23:08.597820

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70d49e82bd76'
down_revision = '9193dfa10046'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('fname', sa.String(length=100), nullable=True))
    op.add_column('user', sa.Column('lname', sa.String(length=100), nullable=True))
    op.create_unique_constraint(None, 'user', ['lname'])
    op.create_unique_constraint(None, 'user', ['fname'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'lname')
    op.drop_column('user', 'fname')
    # ### end Alembic commands ###