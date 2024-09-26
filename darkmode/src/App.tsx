import LightModeIcon from '@mui/icons-material/LightMode';

function App(){


    return(
        <div className="bg-white h-screen flex items-center justify-around">
            <LightModeIcon className='fixed top-20' sx={{ fontSize: 40 }}/>
            <h1 className="font-serif text-bold text-[20rem] ">Bonjour</h1>
            <div className="flex flex-col justify-center pt-14">
                <a href="" className="text-xl font-lg font-serif hover:border-b hover:border-black transition">Home</a>
                <a href="" className="text-xl font-lg font-serif hover:border-b hover:border-black transition">Services</a>
                <a href="" className="text-xl font-lg font-serif hover:border-b hover:border-black transition">About</a>
                <a href="" className="text-xl font-lg font-serif hover:border-b hover:border-black transition">Contact</a>
            </div>
        </div>
    );


}

export default App