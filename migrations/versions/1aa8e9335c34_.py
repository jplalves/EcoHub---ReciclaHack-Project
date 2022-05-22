"""empty message

Revision ID: 1aa8e9335c34
Revises: 
Create Date: 2022-05-21 23:11:52.219888

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1aa8e9335c34'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cooperative',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('email', sa.String(length=84), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.Column('fantasy_name', sa.String(length=128), nullable=True),
    sa.Column('cep', sa.String(length=20), nullable=True),
    sa.Column('address', sa.String(length=128), nullable=True),
    sa.Column('complement', sa.String(length=128), nullable=True),
    sa.Column('cnpj', sa.String(length=20), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('garbage',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=False),
    sa.Column('type_of_garbage', sa.String(length=15), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('email', sa.String(length=84), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('cep', sa.String(length=20), nullable=True),
    sa.Column('address', sa.String(length=128), nullable=True),
    sa.Column('complement', sa.String(length=128), nullable=True),
    sa.Column('cpf_or_cnpj', sa.String(length=20), nullable=True),
    sa.Column('birth_date', sa.Date(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('comments',
    sa.Column('garbage_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('cooperative_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('message', sa.String(length=1500), nullable=True),
    sa.Column('up_votes', sa.Integer(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['cooperative_id'], ['cooperative.id'], ),
    sa.ForeignKeyConstraint(['garbage_id'], ['garbage.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comment_likes',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('comment_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('cooperative_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['comment_id'], ['comments.id'], ),
    sa.ForeignKeyConstraint(['cooperative_id'], ['cooperative.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comment_likes')
    op.drop_table('comments')
    op.drop_table('users')
    op.drop_table('garbage')
    op.drop_table('cooperative')
    # ### end Alembic commands ###
