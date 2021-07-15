import click
from rdkit import Chem
from rdkit.Chem import Crippen


@click.command()
@click.option(
    "--fuzz",
    is_flag=True,
    default=False,
    show_default=True,
    help="Random change logP value by +/- 10%",
)
@click.option(
	"--SMILES", 
	default="CCCCCCCCO",
	#help="ligand SMILES string"
)
@click.option(
        "--output-dir", 
        help="Output Directory", 
        type=click.Path(exists=True)
)

def get_logp(SMILES, fuzz, output_dir):
	rdmol = Chem.MolFromSmiles(SMILES)
	rdlogP = Crippen.MolLogP(rdmol)
	print(rdlogP)



if __name__ == "__main__":
	get_logp()
