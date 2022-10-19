import numpy as np
from scipy.linalg import schur
from network_control.energies import gramian

def node_strength(A):
    """ Returns strength of the nodes of a network.

    Args:
        A: np.array (n_parcels, n_parcels)
            Adjacency matrix from structural connectome

    Returns:
        s: np.array (n_parcels,)
            vector of strength values across nodes

    @author lindenmp
    """
    s = np.sum(A, axis=0)

    return s


def ave_control(A_norm, version=None):
    """ Returns values of AVERAGE CONTROLLABILITY for each node in a network, given the adjacency matrix for that
    network. Average controllability measures the ease by which input at that node can steer the system into many
    easily-reachable states.

    Args:
        A_norm: np.array (n_parcels, n_parcels)
            Normalized adjacency matrix from structural connectome (see matrix_normalization in utils for example)
        version: str
            options: 'continuous' or 'discrete'. default=None

    Returns:
        ac: np.array (n_parcels,)
            vector of average controllability values for each node

    @author lindenmp
    Reference: Gu, Pasqualetti, Cieslak, Telesford, Yu, Kahn, Medaglia,
               Vettel, Miller, Grafton & Bassett, Nature Communications
               6:8414, 2015.
    """

    if version == 'discrete':
        T, U = schur(A_norm, 'real')  # Schur stability
        midMat = np.multiply(U, U).transpose()
        v = np.matrix(np.diag(T)).transpose()
        N = A_norm.shape[0]
        P = np.diag(1 - np.matmul(v, v.transpose()))
        P = np.tile(P.reshape([N, 1]), (1, N))
        ac = sum(np.divide(midMat, P))
    elif version == 'continuous':
        n = A_norm.shape[0]
        G = gramian(A_norm, B=np.eye(n), T=1, version=version)
        ac = G.diagonal()
    elif version == None:
        raise Exception("Time system not specified. "
                        "Please nominate whether you normalized A for a continuous-time or a discrete-time system")

    return ac


def modal_control(A_norm):
    """ Returns values of MODAL CONTROLLABILITY for each node in a network, given the adjacency matrix for that network.
    Modal controllability indicates the ability of that node to steer the system into difficult-to-reach states,
    given input at that node. Expects input to be a DISCRETE system

    Args:
        A_norm: np.array (n_parcels, n_parcels)
            Normalized adjacency matrix from structural connectome (see matrix_normalization in utils for example)

    Returns:
        phi: np.array (n_parcels,)
            vector of modal controllability values for each node

    @author lindenmp
    Reference: Gu, Pasqualetti, Cieslak, Telesford, Yu, Kahn, Medaglia,
               Vettel, Miller, Grafton & Bassett, Nature Communications
               6:8414, 2015.
    """

    T, U = schur(A_norm, 'real')  # Schur stability
    eigVals = np.diag(T)
    N = A_norm.shape[0]
    phi = np.zeros(N, dtype=float)
    for i in range(N):
        Al = U[i,] * U[i,]
        Ar = (1.0 - np.power(eigVals, 2)).transpose()
        phi[i] = np.matmul(Al, Ar)

    return phi
