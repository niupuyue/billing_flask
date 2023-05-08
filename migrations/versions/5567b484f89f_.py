"""empty message

Revision ID: 5567b484f89f
Revises: 
Create Date: 2023-05-08 18:53:48.705915

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5567b484f89f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_base',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='用户ID'),
    sa.Column('deviceid', sa.String(length=255), nullable=True, comment='用户登录的deviceid，游客用户可使用该字段作为唯一标志'),
    sa.Column('username', sa.String(length=20), nullable=True, comment='用户名'),
    sa.Column('realname', sa.String(length=20), nullable=True, comment='真实名字'),
    sa.Column('avatar', sa.String(length=255), nullable=True, comment='头像'),
    sa.Column('remark', sa.String(length=255), nullable=True, comment='备注'),
    sa.Column('password_hash', sa.String(length=128), nullable=True, comment='哈希密码'),
    sa.Column('enable', sa.Integer(), nullable=True, comment='启用'),
    sa.Column('create_at', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('update_at', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('apscheduler_jobs', schema=None) as batch_op:
        batch_op.drop_index('ix_apscheduler_jobs_next_run_time')

    op.drop_table('apscheduler_jobs')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('apscheduler_jobs',
    sa.Column('id', mysql.VARCHAR(collation='utf8mb4_german2_ci', length=191), nullable=False),
    sa.Column('next_run_time', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('job_state', sa.BLOB(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_german2_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('apscheduler_jobs', schema=None) as batch_op:
        batch_op.create_index('ix_apscheduler_jobs_next_run_time', ['next_run_time'], unique=False)

    op.drop_table('user_base')
    # ### end Alembic commands ###
