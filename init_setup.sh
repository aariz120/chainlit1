echo [$(date)]: "START"
echo [$(date)]: "creating a conda env with python 3.10"
conda create -p ./chainenv python=3.10 -y
echo [$(date)]: "created conda env"
source activate ./chainenv
echo [$(date)]: "activated conda env"
echo [$(date)]: "installing requirements"
pip install -r requirements.txt`
echo [$(date)]: "installed all the requirement"
echo [$(date)]: "END"